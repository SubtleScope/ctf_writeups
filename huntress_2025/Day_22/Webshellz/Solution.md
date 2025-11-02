# Prompt

![](/huntress_2025/Day_22/Webshellz/Challenge_Webshellz.png "Challenge Prompt")

# Solution

## Challenge 1

```
Something funky is going on with a new account that was created. Can you find the flag? This flag ends with a 6.
```

- The zip contains a pcap, a evtx log, and a web traffic log. With Windows event files (evtx) Chainsaw is a great utility for this. So my first thought was to look for “net user”. I found the encoded flag (password), but didn’t figure out the encoding until later. It was Base62.

![Chainsaw](/huntress_2025/Day_22/Webshellz/Chainsaw.png "Chainsaw")

- [Base62 CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base62('0-9A-Za-z')&input=VkpHU3VFUmM2cVlBWVBkUmM1NTZKVEhxeHFXd0xiUHd6QUJjMFhnSWhnd1lFV2RRamkx&ieol=CRLF)

![CyberChef 1](/huntress_2025/Day_22/Webshellz/CyberChef_1.png "CyberChef 1")

## Challenge 2

```
There seems to be some Funky Random Program! This flag ends with a d.
```

- I noticed some various exes being uploaded, and then made the connection with Funky Random Program == FRP. At first I had extracted some of them and looked at them, but that was out of scope for this.

![Bin Label 1](/huntress_2025/Day_22/Webshellz/Bin_Label.png "Bin Label 1")

![Bin Label 2](/huntress_2025/Day_22/Webshellz/Bin_Label_2.png "Bin Label 2")

- Triple ===, so probably base32 encoding. 

![CyberChef 2](/huntress_2025/Day_22/Webshellz/CyberChef_2.png "CyberChef 2")

- [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base32('A-Z2-7%3D',true)&input=TVpXR0NaMzNNTTNXRVlKWEdaUlRBWUpVR1E0RElaVEZIQlJUQ01aVk1FWVRDT0pWTVU0R0lPSlVNVlNIMj09PQ&ieol=CRLF)

## Challenge 3

```
How did the threat actor attempt to gain access to the webshell? This flag ends with a e.
```

- I was searching through when the initial shell got uploaded and found what looked to be some Base64 strings. I put them in Cyberchef and got the flag. 

![Event Target](/huntress_2025/Day_22/Webshellz/Event_Target.png "Event Target")

```
__EVENTTARGET=&__FILE=&__VIEWSTATE=%2FwEPDwUKMTg1NzY0NjY1MA8WAh4TVmFsaWRhdGVSZXF1ZXN0TW9kZQIBFgICBA9kFgICAw8WAh4HVmlzaWJsZWgWBgIJD2QWAgIDDxBkZBYBZmQCHQ9kFgQCAg8QZGQWAWZkAgUPZBYCAgMPZBYEAgEPEGRkFgBkAgMPEGRkFgFmZAIhD2QWAgILDxBkZBYBZmRkiHWp84MkXqQMgVs3p3Lcf6EgMVB9%2F9od3kKUDYLmiG8%3D&__VIEWSTATEGENERATOR=590BBAB6&__EVENTVALIDATION=%2FwEdAAO0%2FcoqrnxNs%2B2X0cBnXnyoxqtQhjhXkl7GpTTS3QEoG8IfTMgLVpbR6SeGROGuCp%2FkVaTxwWAU9BfU8kycel9gl04H22Z1wzt2CsWZOTX42A%3D%3D&Bin_TextBox_Login=ZmxhZ3tmYjRlMDc4YTczOWFjNGNlNjg3ZWI3OGMyZTUxYWFmZX0%3D&Bin_Button_Login=Log
```

- [CyberChef Base64](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=Wm14aFozdG1ZalJsTURjNFlUY3pPV0ZqTkdObE5qZzNaV0kzT0dNeVpUVXhZV0ZtWlgw): ZmxhZ3tmYjRlMDc4YTczOWFjNGNlNjg3ZWI3OGMyZTUxYWFmZX0

# Flag

- Something funky is going on with a new account that was created. Can you find the flag? This flag ends with a 6.
  - flag{03638631595684f0c8c461c24b0879e6}
- There seems to be some Funky Random Program! This flag ends with a d.
  - flag{c7ba76c0a4484fe8c135a1195e8d94ed}
- How did the threat actor attempt to gain access to the webshell? This flag ends with a e.
  - flag{fb4e078a739ac4ce687eb78c2e51aafe}