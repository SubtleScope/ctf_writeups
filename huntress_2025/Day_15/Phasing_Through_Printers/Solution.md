# Prompt

![](/huntress_2025/Day_15/Phasing_Through_Printers/Challenge_PhasingThroughPrinters.png "Challenge Prompt")

# Solution

- My first thought was to look for the setuid bit on a file. I couldn’t find it originally, but then I thought to look in /bin, /usr/bin/, and /usr/local/bin. In /usr/local/bin, there was an admin_help file. When you run it, it says: `“Your wish is my command... maybe :) Bad String in File.”`. Running strings resulted in some strings being shown, specifically: `chmod +x /tmp/wish.sh && /tmp/wish.sh`. So if we add our cat command to the file, we’ll then execute the script and get the flag.

```
; ls -la /usr/local/bin
; strings /usr/local/bin/admin_help
; echo "cat /root/flag.txt" >> /tmp/wish.sh
; /usr/local/bin/admin_help
```

![Strings](/huntress_2025/Day_15/Phasing_Through_Printers/Strings.png "Strings" )

![Output - Flag](/huntress_2025/Day_15/Phasing_Through_Printers/Output.png "Output - Flag")

# Flag

- flag{93541544b91b7d2b9d61e90becbca309}