# Bomb Squad Write Up

## Synopsis
  Solve multiple (4) defusions to get the flag

## Background
  Your objective is to defuse the bomb

## Solution

### Part 1
- Enter a number that, when passed through a multiply/shift/divide routine, evaluates to 1337 (e.g., 8599).
- `r2 ./bomb_squad`
  - [0x08048630]> `aaaa`
  - [0x08048630]> `pdf @ main`
    - Output:
    ```
    0x08048c96      e81bfdffff     call sym.phase_1 <br />
    ....
  - [0x08048630]> `pdf @ sym.phase1`
    - Output:
    ```
    0x080489bc      c70424ac8e04.  mov dword [esp], str.Give_me_a_number_ ; [0x8048eac:4]=0x65766947 LEA str.Give_me_a_number_ ; "Give me a number!" @ 0x8048eac <br />
    ....
    0x08048a07      817df4390500.  cmp dword [ebp - local_ch], 0x539 ; [0x539:4]=0xe0e90000 <br />
    ....
    ```
  - From this, we know that we are expected to provide the program a number and that at the location [ebp - local_ch], the value must equal 1337
  - $ `rax2 0x539`
    - Output: <br />
    ```1337``` 
  - Some python to reproduce the math of the bomb logic, you can select any number in this range.
    ```python
    def phase1(x: int) -> int:
    q = (2 * x) // 37 
    return (q - 18) * 3 - 1

    for x in range(0, 20000):
        if phase1(x) == 1337:
            print("Valid input:", x)
    ```
  - $ `./bomb_squad`
    - Output:
    ```
    Welcome to the bomb squad! Your first task: Diffuse this practice bomb.
    Give me a number!
    8599
    You got through phase 1 alright! Good work! But can you handle phase 2?
    ```
## Part 2
  - Provide an array of six numbers that satisfy a recursive rule where each pair sums to a power of two ([1, 1, 3, 5, 11, 21]).
  - You can use this python to produce the array you need based on the logic from the code:
  ```python
  def func2(i: int) -> int:
      # returns 2^i
      return 1 << i
  
  def check_phase2(arr):
      if len(arr) != 6:
          return False
      if arr[0] != 1:
          return False
      for i in range(1, 6):
          if arr[i-1] + arr[i] != func2(i):
              return False
      return True
  
  def derive_phase2():
      a = [0]*6
      a[0] = 1
      for i in range(1, 6):
          a[i] = (1 << i) - a[i-1]
      return a
  
  # Demo
  sol = derive_phase2()
  print(sol)                 # [1, 1, 3, 5, 11, 21]
  print(check_phase2(sol))   # True
  ```
  - `[1, 1, 3, 5, 11, 21]`

## Part 3
  - Input a lowercase string that, when run through a substitution lookup table, matches an embedded ciphertext (mappingstringsforfunandprofit).
  - Here's some python to handle the logic of Part 3:
  ```python
  keys   = "qagvCYiheXulrpszNLwMtodbVx"   # maps a..z -> keys[i]
  target = "rqzzepiwMLepiwYsLYtpqpvzLsYeM"
  
  # Build inverse map: target byte -> plaintext letter in 'a'..'z'
  inv = {keys[i]: chr(ord('a') + i) for i in range(26)}
  
  # Decode the required plaintext input
  plaintext = "".join(inv[ch] for ch in target)
  print(plaintext)  # -> mappingstringsforfunandprofit
  
  def check_phase3(user_input: str) -> bool:
      if any(not ('a' <= ch <= 'z') for ch in user_input):
          return False
      if len(user_input) != len(target):
          return False
      for ch_in, ch_tgt in zip(user_input, target):
          idx = ord(ch_in) - ord('a')
          if keys[idx] != ch_tgt:
              return False
      return True
  
  assert check_phase3("mappingstringsforfunandprofit")
  ```
## Part 4
  - Give seven integers (each 0–3) that guide a traversal through a small weighted node graph such that the total accumulated weight equals 95 (0 0 0 1 1 2 1).
  ```
  [0xf7ee9579]> px 28 @ 0x804b070
  - offset -  7071 7273 7475 7677 7879 7A7B 7C7D 7E7F  0123456789ABCDEF
  0x0804b070  8cb0 0408 a8b0 0408 c4b0 0408 e0b0 0408  ................
  0x0804b080  4e31 0000 0000 0000 0a00 0000            N1..........
  [0xf7ee9579]> px 28 @ 0x804b08c
  - offset -  8C8D 8E8F 9091 9293 9495 9697 9899 9A9B  CDEF0123456789AB
  0x0804b08c  a8b0 0408 c4b0 0408 e0b0 0408 fcb0 0408  ................
  0x0804b09c  4e32 0000 0000 0000 0700 0000            N2..........
  [0xf7ee9579]> px 28 @ 0x804b0a8   # n3
  - offset -  A8A9 AAAB ACAD AEAF B0B1 B2B3 B4B5 B6B7  89ABCDEF01234567
  0x0804b0a8  70b0 0408 8cb0 0408 c4b0 0408 fcb0 0408  p...............
  0x0804b0b8  4e33 0000 0000 0000 0900 0000            N3..........
  [0xf7ee9579]> px 28 @ 0x804b0c4   # n4
  - offset -  C4C5 C6C7 C8C9 CACB CCCD CECF D0D1 D2D3  456789ABCDEF0123
  0x0804b0c4  c4b0 0408 c4b0 0408 c4b0 0408 c4b0 0408  ................
  0x0804b0d4  4e34 0000 0000 0000 0200 0000            N4..........
  [0xf7ee9579]> px 28 @ 0x804b0e0   # n5
  - offset -  E0E1 E2E3 E4E5 E6E7 E8E9 EAEB ECED EEEF  0123456789ABCDEF
  0x0804b0e0  70b0 0408 fcb0 0408 70b0 0408 fcb0 0408  p.......p.......
  0x0804b0f0  4e35 0000 0000 0000 1000 0000            N5..........
  [0xf7ee9579]> px 28 @ 0x804b0fc   # n6
  - offset -  FCFD FEFF  0 1  2 3  4 5  6 7  8 9  A B  CDEF0123456789AB
  0x0804b0fc  fcb0 0408 fcb0 0408 fcb0 0408 fcb0 0408  ................
  0x0804b10c  4e36 0000 0000 0000 1b00 0000            N6..........
  ```
## Solution
  - <img width="793" height="293" alt="image" src="https://github.com/user-attachments/assets/fea49907-dd0d-4a5c-9942-92adb5316ea9" />
