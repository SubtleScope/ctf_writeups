# Rev2 Write Up

## Synopsis
  Reverse Engineering Challenge, find the flag

## Background
  Find the flag, the flag is not in the standard sctf{xxxx} format. You must put it in the flag format.

## Solution
  - $ `r2 ./rev2`
  - Output:
    .... <br />
    0x0040066c      bfa4074000     mov edi, str.What_is_the_magic_password_ ; "What is the magic password?" @ 0x4007a4 <br />
    .... <br />
    0x0040068f      3d83da0d03     cmp eax, 0x30dda83 <br />
    .... <br />
    0x00400702      bfc3074000     mov edi, str.Correct__Your_flag_is:__d ; "Correct! Your flag is: %d" @ 0x4007c3 <br />
    ....
  - So we know that unlike rev1, rev2 expects a number/digit
  - We can attempt to get the required input by looking at the cmp statement
  - $ `rax2 0x30dda83`
  - Output: <br />
    51239555
  - $ `./rev2`
  - Output: <br />
    What is the magic password? <br />
    51239555 <br />
    Correct! Your flag is: 51196695 <br />

  - Flag: sctf{51196695}

  - Part 1: <br />
    ![Part1](rev2_part1.jpg?raw=true "Part1") <br />
  - Part 2: <br />
    ![Part2](rev2_part2.jpg?raw=true "Part2") <br />
  - Part 3: <br />
    ![Part3](rev2_part3.jpg?raw=true "Part3") <br />
