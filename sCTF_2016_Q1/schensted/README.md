# Schensted Write Up

## Synopsis
  Find the longest non-decresing substring. The answer is not in the normal sctf{xxxx} format, so you need to put it into the proper flag format

## Source
  Code has been adapted from (user: dparpyani): <br />
  http://codereview.stackexchange.com/questions/33291/improving-efficiency-for-finding-longest-contiguous-non-decreasing-substring

## Solution (Unsolved)
  - $ `python seq.py`
  - Output: <br />
    112233346778

## Notes
  I did not solve this challenge, but believe I was on the right track.

## Code
  - The code finds the longest nondecresing substring.
  - I modified the code to support all possibilities (non-decreasing and decreasing).
  - The Output for each case below is the output using the schensted.dat file
    - Find the longest non-decreasing substring (with duplicates)
        * If a character is greater or equal to the previous one <br />
        * 89011356781923 => 01135678 <br >
        * `if character >= current_sequence[-1]:`<br />
        * Output: 112233346778
    - Find the longest non-decresing substring (without duplicates)
        * If character is greater than the previous one <br />
        * 89011356781923 => 135678 <br />
        * `if character > current_sequence[-1]:` <br />
        * Output: 01235678
    - The following are not part of the challnege, but wanted to test it anyway
    - Find the longest decreasing substring (with duplicates)
        * If a character is less than or equal to the previous one <br />
        * 02349985543928 => 9985543 <br />
        * `if character <= current_sequence[-1]:` <br />
        * Output: 8774444444200
    - Find the longest decreasing substring (without duplicates)
        * If a character is less than the previous one <br />
        * 02348962191 => 9621 <br />
        * `if character < current_sequence[-1]:` <br />
        * Output: 8765420
