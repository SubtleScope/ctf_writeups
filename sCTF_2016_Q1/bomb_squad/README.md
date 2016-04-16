# Bomb Squad Write Up

## Synopsis
  Solve multiple (4) defusions to get the flag

## Background
  Your objective is to defuse the bomb

## Partial Solution
  - $ `r2 ./bomb_squad`
  - [0x08048630]> `aaaa`
  - Output:
    [x] Analyze all flags starting with sym. and entry0 (aa)
    [x] Analyze len bytes of instructions for references (aar)
    ....
  - [0x08048630]> `pdf @ main`
  - Output: 
    ....
    0x08048c96      e81bfdffff     call sym.phase_1
    ....
  - [0x08048630]> `pdf @ sym.phase1`
  - Output:
    0x080489bc      c70424ac8e04.  mov dword [esp], str.Give_me_a_number_ ; [0x8048eac:4]=0x65766947 LEA str.Give_me_a_number_ ; "Give me a number!" @ 0x8048eac
    ....
    0x08048a07      817df4390500.  cmp dword [ebp - local_ch], 0x539 ; [0x539:4]=0xe0e90000
    ....
  - From this, we know that we are expected to provide the program a number and that at the location [ebp - local_ch], the value must equal 1337
  - $ `rax2 0x539`
  - Output:
    1337
  - So, through some trial and error, we must submit a value of `8599` in order to pass the first round.
  - $ `./bomb_squad`
  - Output:
    Welcome to the bomb squad! Your first task: Diffuse this practice bomb.
    Give me a number!
    8599
    You got through phase 1 alright! Good work! But can you handle phase 2?

## Notes
  - I did not solve this challenge, but wanted to provide/share this with the public
  - I got past the first defusion, but did not get past that point and did not have much time to work on the second phase (and so on)
