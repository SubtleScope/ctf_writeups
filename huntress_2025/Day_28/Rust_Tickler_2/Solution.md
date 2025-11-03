# Prompt

![](/huntress_2025/Day_28/Rust_Tickler_2/Challenge_RustTickler2.png "Challenge Prompt")

# Solution

- This one was fun and a little annoying, lol. So I noticed pretty quickly, there was some sort of mapping/lookup table based on the varying “A” values I saw being loaded into r8. See below: 

![IDA - R8 - A's](/huntress_2025/Day_28/Rust_Tickler_2/r8_As.png "IDA - R8 - A's")

- I found Bingus early on and entered it, but got the correct message and no flag. Changing the A values (as seen below), got me a bunch of the various messages but no flag. 

```
0xAAAA              => "Bingus"
0xAAAAA             => "Correct, but that is not the flag..."
0xAAAAAA            => "Wrong, that's not my favorite cat..."
0xAAAAAAA           => "Breaks/Crashes"
0xAAAAAAAA          => "Who is my favorite cat?"
0xAAAAAAAAA         => "Who is my favorite cat?"
0xAAAAAAAAAA        => "Who is my favorite cat?"
0xAAAAAAAAAAAAAAAA  => "Who is my favorite cat?"
```

![Program Output](/huntress_2025/Day_28/Rust_Tickler_2/Program_Output.png "Program Output")

- I had played with modifying the values of r8, but really, we need the proper values from the table to actually retrieve the flag. sub_7FF72C623EA0 is where the mapping is loaded. After some runs, I saw that it was verifying the magic header “HNTS”. After that, I looked at the hex and built out the mapping of the values/table.

![Magic Header](/huntress_2025/Day_28/Rust_Tickler_2/Magic_Header.png "Magic Header")

- This shows the magic header. If you view the hex view, you can start seeing the values/mapping.

![Key Mapping](/huntress_2025/Day_28/Rust_Tickler_2/Key_Mapping.png "Key Mapping")

- From that, we actually build the mapping like below. The condensed list is below that.

```
0xA9 -> "Please don't look in the icon file!"
0x9F -> "The ducks are unionizing!"
0xA1 -> "I am totally a blue herring"
0x83 -> "The flag is the hash of the name of a certain Infosec YouTuber"
0x7F -> "flag{f59a5f604d236425490133c3fac89a88}"
0x40 -> "Crab tickler!"
0x51 -> "The flag is protected!"
```

- So I set the value of r8 to 0x7F and voila and I got the flag value. The sub_7FF72C6249C0 function is where the message is called, so we just execute the program to that point and get the flag. 

![Flag](/huntress_2025/Day_28/Rust_Tickler_2/Flag.png "Flag")

- Here’s a view of the two function calls that were needed/useful for determining what was going on:

![Functions](/huntress_2025/Day_28/Rust_Tickler_2/Functions.png "Functions")

# Flag

- flag{f59a5f604d236425490133c3fac89a88}