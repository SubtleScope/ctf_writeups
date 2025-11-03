# Prompt

![](/huntress_2025/Day_28/Telestealer/Challenge_Telestealer.png "Challenge Prompt")

# Solution

- Pretty simple. Follow the decode path of JScript => PowerShell => Executable.
- I joined the lines myself, but you could modify the JScript to do that. Decode the code down to the powershell, but delete the execution line. Then grab the x.exe final payload. From that, you can use ILSpy to decode and analyze the C# which leads you to a Telegram bot. You don’t actually try to get any files, but if you message the bot, it will ask you a question. 

![ILSpy](/huntress_2025/Day_28/Telestealer/ILSpy.png "ILSpy")

- Piece together the variables and link - or, rather, grab the botname and message it on Telegram. Answer the question and get the flag value. 

![Telegram](/huntress_2025/Day_28/Telestealer/Telegram.png "Telegram")

# Flag

- flag{5f5b173825732f5404acf2f680057153}