# Prompt

![](/huntress_2025/Day_03/SANDY/Challenge_SANDY.png "Challenge Prompt")

# Solution

- I originally ran this in IDA as well as some other programs to see what was going on. I kept seeing AU3, but didn’t go look into it originally. That was a mistake. It wasn’t until I started looking at the overlay and saw some AutoIt stuff that Start by downloading and analyzing the file. Upon a quick analysis, we can see SANDY is UPX packed. So let’s unpack it. 

```bash
unzip SANDY.zip
upx -d SANDY.exe
```

- After unpacking, we see a suspicious overlay which is actually an AutoIt script.

![Step 2](/huntress_2025/Day_03/SANDY/Step_2_AutoIT.png "Step 2")

- So this AutoIt seems to be encrypted/obfuscated in some way. I found a tool [myAutToExe](https://github.com/daovantrong/myAutToExe). When I added the executable to the program, it spit out a log and the au3 (autoit) script. Looking at the script, there is a big section of base64 chunks:

![Step 3](/huntress_2025/Day_03/SANDY/Step_3_base64_Chunks.png)

- Clean up the base64 and use this [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)Decode_text('UTF-16LE%20(1200)')&ieol=CRLF&oeol=CRLF) link to decode it. You now get more Base64 to sort through. 

![Step 4](/huntress_2025/Day_03/SANDY/Step_4_Powershell_Code.png "Step 4")

- This base64 decoded provides a flag value: 

![Step 5-1](/huntress_2025/Day_03/SANDY/Step_5_Code_Output_1.png "Step 5-1")

![Step 5-2](/huntress_2025/Day_03/SANDY/Step_5_Code_Output_2.png "Step 5-2")

- In other cases, remove the Invoke-Expression command and output the decrypted function: 

![Alternate - Step 1](/huntress_2025/Day_03/SANDY/Step_6_Alternate.png "Alternate - Step 1")

- You could do this with Python, but I just manually did it with PowerShell. Some of these produce junk data which I wasted some time on:

![Alternate - Step 2](/huntress_2025/Day_03/SANDY/Step_7_Alternate.png "Alternate - Step 2")

# Flag

- flag{27768419fd176648b335aa92b8d2dab2}