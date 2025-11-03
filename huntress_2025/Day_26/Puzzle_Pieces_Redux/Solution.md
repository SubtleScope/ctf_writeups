# Prompt

![](/huntress_2025/Day_26/Puzzle_Pieces_Redux/Challenge_PuzzlePiecesRedux.png "Challenge Prompt")

# Solution

- This one wasn’t too bad, but I was pretty slow/bad with my command line fu, so I ended up just doing some things manually. Extract the files and you’ll see they are all Windows PE files. 

![File Check](/huntress_2025/Day_26/Puzzle_Pieces_Redux/File_check.png "File Check")

- So I ran them on my Windows host and got all of the flag components except for the 4fb.. File. That one had some issues, but didn’t ultimately matter. I did find the string value based on its location in the other executables though. Anyway, I actually found the flag string in Malcat, but then switched back to Kali and ran grep -rnai flag *. I found that the files had some debug data: flag_part_#.pdb.

![Flag Part](/huntress_2025/Day_26/Puzzle_Pieces_Redux/Flag_Part.png "Flag Part")

- I then did some command line to sort the order of all the flag parts. 

```shell
grep -rnao "flag_part_[0-9]" | awk -F':' '{ print $3, $1 }' | sort

# Output                                           
flag_part_0 945363af.bin
flag_part_0 c8c5833b33584.bin
flag_part_1 5e47.bin
flag_part_1 8208.bin
flag_part_2 4fb72a1a24.bin
flag_part_2 7b217.bin
flag_part_3 5fa.bin
flag_part_3 e1204.bin
flag_part_4 8c14.bin
flag_part_4 a4c71d6229e19b0.bin
flag_part_5 24b429c2b4f4a3c.bin
flag_part_5 aa60783e.bin
flag_part_6 53bc247952f.bin
flag_part_6 f12f.bin
flag_part_7 c54940df1ba.bin
flag_part_7 d2f7.bin
```

- From this, I figured it would be something with the timing, so I ran this (note output is cleaned up for formatting):

```shell
for x in $(grep -rnao "flag_part_[0-9]" | awk -F':' '{ print $1 }' | sort); do echo "${x}"; exiftool "${x}" | grep -i "time stamp" | awk -F' ' '{ print $5 }' ; done;

# Output 

24b429c2b4f4a3c.bin 11:46:56-04:00
4fb72a1a24.bin      <nothing>
53bc247952f.bin     11:46:56-04:00
5e47.bin            11:46:57-04:00
5fa.bin             11:46:57-04:00
7b217.bin		    11:46:55-04:00
8208.bin		    11:46:55-04:00
8c14.bin		    11:46:57-04:00
945363af.bin		11:46:56-04:00
a4c71d6229e19b0.bin	11:46:56-04:00
aa60783e.bin		11:46:57-04:00
c54940df1ba.bin 	11:46:56-04:00
d2f7.bin		    11:46:58-04:00
e1204.bin		    11:46:55-04:00
f12f.bin		    11:46:58-04:00
```

- Executing them on Windows got me these various flag parts. Everyone was 5 hex chars + the byte 0x0A. I add that last part because that’s how I found the missing part from the 4fb executable.

![Program Run](/huntress_2025/Day_26/Puzzle_Pieces_Redux/Program_run.png "Program Run")

- So I manually sorted them and combined them to get the flag:

```
c8c5833b33584.bin	11:46:55-04:00  flag{
8208.bin		    11:46:55-04:00  be7a1
7b217.bin		    11:46:55-04:00  e6817
e1204.bin		    11:46:55-04:00  d85d5
a4c71d6229e19b0.bin	11:46:56-04:00  49f8b
24b429c2b4f4a3c.bin 11:46:56-04:00  5abfa
53bc247952f.bin     11:46:56-04:00  f18ba
c54940df1ba.bin	    11:46:56-04:00  02}

flag{be7a1e6817d85d549f8b5abfaf18ba02}
```

![Flag Parts](/huntress_2025/Day_26/Puzzle_Pieces_Redux/Flag_Parts.png "Flag Parts")

# Flag

- flag{be7a1e6817d85d549f8b5abfaf18ba02}