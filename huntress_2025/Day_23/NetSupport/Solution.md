# Prompt

![](/huntress_2025/Day_23/NetSupport/Challenge_NetSupport.png "Challenge Prompt")

# Solution

- This one is pretty easy and straightforward. Look at the Powershell code and see what it does: 

![Powershell](/huntress_2025/Day_23/NetSupport/Powershell.png "Powershell")

- Essentially, it creates a WAV file, renames it to zip, and then creates an execution chain to bypass defenses and hide its execution. It attempts to run (and clean up after itself) client32.exe. If you execute the first part to get the zip and then look at the files, you will see client32.exe and the client32.ini. If you were to attempt to execute client32.exe, you will get an error message about the checksum of client32.ini. 

- Look at client32.ini and you will find the encoded flag value aptly named Flag. 

![Flag Decoded](/huntress_2025/Day_23/NetSupport/Decoded.png "Flag Decoded")

- Throw that in your favorite base64 decoder and get the flag 

```
ZmxhZ3tiNmU1NGQwYTBhNWYyMjkyNTg5YzM4NTJmMTkzMDg5MX0NCg==
flag{b6e54d0a0a5f2292589c3852f1930891}
```

# Flag

- flag{b6e54d0a0a5f2292589c3852f1930891}