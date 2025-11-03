# Prompt

![](/huntress_2025/Day_23/Rust_Tickler/Challenge_RustTickler.png "Challenge Prompt")

# Solution

## Original Solution

- I loaded this in IDA and began to run through it. Early on, it gets to a function where it compares user input to the flag value. The program does ask you for the flag value and will tell you you’re correct. 

![IDA](/huntress_2025/Day_23/Rust_Tickler/IDA.png "IDA")

![Solution](/huntress_2025/Day_23/Rust_Tickler/Solution.png "Solution")

## Alternative Solution

- You could also have easily (I did not, but saw the string), found this string and XOR’ed it to get the flag value even faster. See [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Hex','string':'51'%7D,'Standard',false)&input=MzczRDMwMzYyQTY3NjE2NzY3MzMzMDY0MzAzMzY3NjYzMjYwNjYzNTY3MzU2NDYyNjEzMzYzMzA2ODY4NjM2NDMyNjM2MDM0NjI&ieol=CRLF&oeol=CRLF).

![CyberChef](/huntress_2025/Day_23/Rust_Tickler/CyberChef.png "CyberChef")

- You can find the required XOR key in the binary as well or just use the [CyberChef XOR Bruteforce](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR_Brute_Force(1,100,0,'Standard',false,true,false,'')&input=MzczRDMwMzYyQTY3NjE2NzY3MzMzMDY0MzAzMzY3NjYzMjYwNjYzNTY3MzU2NDYyNjEzMzYzMzA2ODY4NjM2NDMyNjM2MDM0NjI&ieol=CRLF&oeol=CRLF). 

# Flag

- flag{6066ba5ab67c17d6d530b2a9925c21e3}