# Prompt

![](/huntress_2025/Day_07/Trust_Me/Challenge_TrustMe.png "Challenge Prompt")

# Solution

## Simplest/Fastest Solution

- You could have solved this in a couple of minutes with this [NirSoft](https://www.nirsoft.net/utils/advanced_run.html) tool. You run the code to base64 encode the executable, decode it on the target, and then set the options to run TrustMe.exe as TrustedInstaller with the software. 

- On your attack box: run this, then clean up the cert banners and newlines. Copy to the target host (2 times due to copy buffers)

```shell
certutil -encodehex C:\Windows\System32\AdvancedRun.exe C:\AdvancedRun.hex 0
```

- On the target, run

```powershell
$b64 = Get-Content -Raw .\RunAsSpecial.b64
[System.IO.File]::WriteAllBytes('C:\RunAsSpecial.exe',[System.Convert]::FromBase64String($b64))
```

![Solution](/huntress_2025/Day_07/Trust_Me/Solution_Nirsoft.png "Solution")

## Original Solution/Write Up

-  I tried so many ways to get the correct Trusted Installer role, but to no avail. So I did what I know best. I smuggled the binary out of the VM using the code below and started analyzing it. This is probably not the way to solve this one, but it got me the flag. 

```powershell
certutil -encodehex C:\Windows\System32\TrustMe.exe C:\TrustMe.hex 0
```

- I was then able to copy the test from the TrustMe.hex file, manually remove the new lines and cert headers, and then decode the base64 back into a legitimate/working executable. Mind you, hours before this, I had found the encrypted base64 string, the contents of key.bin - extracted out in a different, but similar manner by saving the raw bytes as base64 encoded ASCII, and copying that over to my reversing host. So all I had to do was drop the file in the same location that the binary expected and load it in IDA, to bypass the TrustedInstaller piece. It took one RIP change to then get to the decrypt functions. 

Based on the Malcat information below, I had everything but the IV. I tried a bunch of strings I suspected to no avail. I kept trying different things and getting a partially decrypted flag, but I needed the IV. So eventually, I was able to get that from IDA and decrypt the flag. The screenshot and code are below.

![Malcat View](/huntress_2025/Day_07/Trust_Me/Step_2_Malcat_View.png "Malcat View")

Here is the code and the screenshot. You will need the key.bin file (or you can change the code to use this string: 

```python
key = bytes.fromhex(‘c5c93bdb841534fae5545edcb0f12041d10cd4d90ee16a7d8235fa657c93825d’)
```

```python
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
import base64

def decrypt(key, iv, ciphertext):
    decipher = AES.new(key, AES.MODE_CBC, iv)
    padded_decrypted_data = decipher.decrypt(ciphertext)

    decrypted_data = unpad(padded_decrypted_data, AES.block_size)
    return decrypted_data

if __name__ == '__main__':
    with open('key.bin', 'rb') as key_file:
        key = key_file.read()

    print(f"Loaded key: {key.hex()}")

    ciphertext = base64.b64decode("Wx6eETGXddnmCT4qZ7BxgRYpC+kdjjFzXxW+BM4HiI3GPaslpFBnpk9XplnaSxNg")
    iv = bytes.fromhex('04C9E65365568D0F8A02F526BA00FC5B')

    decrypted_message = decrypt(key, iv, ciphertext)
    print(f"\nDecrypted message: {decrypted_message}")
```

- This is the cleaned up output and script, trust me, it was not this nice before and had all kinds of test IVs. Again, I got the IV in IDA, cleaned it up, and then plugged it into the script. 

![Step 3](/huntress_2025/Day_07/Trust_Me/Step_3_Flag_Output.png "Step 3")

- IV Hex: 04C9E65365568D0F8A02F526BA00FC5B

![Original Step 1](/huntress_2025/Day_07/Trust_Me/Step%204_IDA_View.png "Original Step 1")

- Going down my original path of looking for the IV in the executable was wrong and cost me some time. Unfortunately, I thought it might be stored there, but it appears, upon a search for the bytes/hex, that it is not, or at least not directly. 

If you had solved it the correct way, you would have eventually been led to this screen (these strings are also in the original Malcat hex/ascii within the binary).

![Original Step 2](/huntress_2025/Day_07/Trust_Me/Step_5_flag.png "Original Step 2")

- This would then allow you to copy the flag and submit it.

## Failed Attempts

```
call    ConvertStringSidToSidA
…

loc_7FF6238D141E:       ; SidToCheck
mov     rdx, [rsp+108h+Sid]
lea     r8, [rsp+108h+IsMember] ; IsMember
mov     [rsp+108h+IsMember], r14d
call    cs:CheckTokenMembership
test    eax, eax
jnz     short loc_7FF6238D1468

cmp     [rsp+108h+IsMember], r14d
jnz     short loc_7FF6238D14A0
```

- Here it would lead to the path that says you need to Trusted Installer, but we can set RIP to the other instruction and everything will then fall into place and grant you the flag. Given that you have the key.bin file in the correct place: `C:\ctf\key.bin`. 
- I tried copying in the psexec binary in as well using a similar method, but it was earlier on and did not work because of how I was converting the binaries to Base64.

Here’s some of what I tried:

```powershell
$action = New-ScheduledTaskAction -Execute "C:\Windows\System32\TrustMe.exe"
Register-ScheduledTask -TaskName 'TI_Exec' -Action $action

$svc = New-Object -ComObject 'Schedule.Service'
$svc.Connect()
$user = 'NT SERVICE\TrustedInstaller'

$folder = $svc.GetFolder('\')
$task = $folder.GetTask('TI_Exec')
$task.RunEx($null, 0, 0, $user)
```

- I set the owner to ‘NT SERVICE\TrustedInstaller’ as well as gave it rights to access the file (full control)/ But with no luck. See [here](https://superuser.com/questions/1643290/how-do-you-run-an-application-as-trustedinstaller-or-system-without-using-extern). But this is not Interactive so there was no way to see if it worked. I tried a lot of things. A lot of manual scheduled tasks as SYSTEM/as TrustedInstaller to no avail which is why I resorted to doing it the way I did. 

- What I should have tried... Getting this on the target: https://github.com/fafalone/RunAsTrustedInstaller.

# Flag

- flag{c6065b1f12395d526595e62cf1f4d82a}