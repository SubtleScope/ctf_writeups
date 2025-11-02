# Prompt

![](/huntress_2025/Day_21/Follow_The_Money/Challenge_FollowTheMoney.png "Challenge Prompt")

# Solution

-Download and unzip the file. We see there are some interesting email files (.eml), if we analyze the files, specifically 5, we can see that there is a domain squatting link similar to the actual link. I used: [EML Analyzer](https://eml-analyzer.herokuapp.com/) to analyze the files, but you could have just grepped the files for the links.

![ls](/huntress_2025/Day_21/Follow_The_Money/ls.png "ls")

![Domain Impersonation](/huntress_2025/Day_21/Follow_The_Money/Malicious_Domain.png "Domain Impersonation")

- If you notice in email 5, the URI points to https://evergatetltle.netlify.app/ instead of the correct URI: https://evergatetitle.netlify.app/. 

- So if you go to the malicious URI and look at the source (notice the hacker/Matrix text, lol):

![Hacker](/huntress_2025/Day_21/Follow_The_Money/Hacker.png "Hacker")

- Decode the base64 and viola, you have the hacker name: `n0trustx`

- Go to the blog and find the hacker’s Github:

![Hacker Blog](/huntress_2025/Day_21/Follow_The_Money/Hacker_Blog.png "Hacker Blog")

- If you inspect the Github link, you will find an HTML page with, you guessed it, another base64 string with the flag.

![Hacker Github](/huntress_2025/Day_21/Follow_The_Money/Hacker_Github.png "Hacker Github")

![Hacker Base64](/huntress_2025/Day_21/Follow_The_Money/Encoded_Base64.png "Hacker Base64")

- Decode the base64 and get the flag.

![Flag](/huntress_2025/Day_21/Follow_The_Money/Flag.png "Flag")

# Flag

- flag{kl1zklji2dycqedj6ef6ymlrsf180d0f} 