# Prompt

![](/huntress_2025/Day_ "Challenge Prompt")

# Solution

- We’re told it’s some sort of encryption/decryption challenge centered around cats. I did some initial analysis and since we had so many images, I figured they were a part of it. 

![Exiftool](/huntress_2025/Day_17/vx-underground/Initial.png "Exiftool")

```
ls
exiftool prime_mode.jp | grep -i comment
exiftool 'Cat Archive'/* | grep -i comment | head -n 2
exiftool 'Cat Archive'/* | grep -i "user comment" >> comments.txt
sort -n comments.txt >> sorted.txt 
```

- I’m not the strongest when it comes to dealing with primes and the crypto-esque challenges like this one. So I plugged it into ChatGPT which conveniently spit out the password to the flag.zip file: 

```python
#!/usr/bin/env python3
"""
Reconstructs AES key / ZIP password from Shamir-style shares.

Input: sorted.txt  (lines like '253-6ba02f81b0c38473b0...')
Prime modulus from challenge: 010000000000000000000000000000000000000000000000000000000000000129
"""

from pathlib import Path

# ---- Load shares ----
path = Path("sorted.txt")
lines = [ln.strip() for ln in path.read_text().splitlines() if ln.strip()]
xs, ys = [], []
for line in lines:
    i_str, hex_str = line.split("-", 1)
    xs.append(int(i_str))
    ys.append(int(hex_str, 16))

# ---- Given prime modulus ----
p = int("010000000000000000000000000000000000000000000000000000000000000129", 16)

# ---- Lagrange interpolation at x = 0 ----
def lagrange_at_zero(xs, ys, p):
    total = 0
    k = len(xs)
    for i in range(k):
        xi, yi = xs[i], ys[i]
        num, den = 1, 1
        for j in range(k):
            if i == j:
                continue
            xj = xs[j]
            num = (num * (-xj)) % p
            den = (den * (xi - xj)) % p
        li0 = (num * pow(den, -1, p)) % p
        total = (total + yi * li0) % p
    return total

secret = lagrange_at_zero(xs, ys, p)

print(f"Recovered secret (hex): {hex(secret)}")

# If it decodes cleanly to ASCII, print that too:
try:
    data = bytes.fromhex(hex(secret)[2:])
    print("ASCII:", data.decode(errors="ignore"))
except Exception as e:
    print("Could not decode ASCII:", e)
```

- ZIP password: `FApekJ!yJ69YajWs`
- Once you get the decrypted zip file, you get a new file, cute-kitty-noises.txt. 

![Meow](/huntress_2025/Day_17/vx-underground/Meow.png "Meow")

- I did a quick search and found: [Meowlang](https://wixette.github.io/meowlang/) which conveniently comes with an [online interpreter](https://wixette.github.io/meowlang/). So I entered the code and clicked debug, to get the decimal. I used the decimal decoder in [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Decimal('Space',false)Decode_text('UTF-8%20(65001)')&input=MiwgMTA5LCAxLCAwLCAyLCA5NywgMSwgMCwgMiwgMTA4LCAxLCAwLCAyLCAxMTksIDEsIDAsIDIsIDk3LCAxLCAwLCAyLCAxMTQsIDEsIDAsIDIsIDEwMSwgMSwgMCwgMiwgMzIsIDEsIDAsIDIsIDEwNSwgMSwgMCwgMiwgMTE1LCAxLCAwLCAyLCAzMiwgMSwgMCwgMiwgMTA1LCAxLCAwLCAyLCAxMDgsIDEsIDAsIDIsIDEwOCwgMSwgMCwgMiwgMTAxLCAxLCAwLCAyLCAxMDMsIDEsIDAsIDIsIDk3LCAxLCAwLCAyLCAxMDgsIDEsIDAsIDIsIDMyLCAxLCAwLCAyLCA5NywgMSwgMCwgMiwgMTEwLCAxLCAwLCAyLCAxMDAsIDEsIDAsIDIsIDMyLCAxLCAwLCAyLCAxMDIsIDEsIDAsIDIsIDExMSwgMSwgMCwgMiwgMTE0LCAxLCAwLCAyLCAzMiwgMSwgMCwgMiwgMTEwLCAxLCAwLCAyLCAxMDEsIDEsIDAsIDIsIDExNCwgMSwgMCwgMiwgMTAwLCAxLCAwLCAyLCAxMTUsIDEsIDAsIDIsIDEwLCAxLCAwLCAyLCA5OSwgMSwgMCwgMiwgOTcsIDEsIDAsIDIsIDExNiwgMSwgMCwgMiwgMTE1LCAxLCAwLCAyLCAzMiwgMSwgMCwgMiwgOTcsIDEsIDAsIDIsIDExNCwgMSwgMCwgMiwgMTAxLCAxLCAwLCAyLCAzMiwgMSwgMCwgMiwgOTksIDEsIDAsIDIsIDExMSwgMSwgMCwgMiwgMTExLCAxLCAwLCAyLCAxMDgsIDEsIDAsIDIsIDMyLCAxLCAwLCAyLCA5NywgMSwgMCwgMiwgMTEwLCAxLCAwLCAyLCAxMDAsIDEsIDAsIDIsIDMyLCAxLCAwLCAyLCA5OCwgMSwgMCwgMiwgOTcsIDEsIDAsIDIsIDEwMCwgMSwgMCwgMiwgOTcsIDEsIDAsIDIsIDExNSwgMSwgMCwgMiwgMTE1LCAxLCAwLCAyLCAxMCwgMSwgMCwgMiwgMTAyLCAxLCAwLCAyLCAxMDgsIDEsIDAsIDIsIDk3LCAxLCAwLCAyLCAxMDMsIDEsIDAsIDIsIDEyMywgMSwgMCwgMiwgNTEsIDEsIDAsIDIsIDUzLCAxLCAwLCAyLCAxMDAsIDEsIDAsIDIsIDk5LCAxLCAwLCAyLCA5OCwgMSwgMCwgMiwgOTcsIDEsIDAsIDIsIDQ5LCAxLCAwLCAyLCA1MSwgMSwgMCwgMiwgNDgsIDEsIDAsIDIsIDUxLCAxLCAwLCAyLCA1MSwgMSwgMCwgMiwgNTIsIDEsIDAsIDIsIDUzLCAxLCAwLCAyLCA1NywgMSwgMCwgMiwgOTksIDEsIDAsIDIsIDk3LCAxLCAwLCAyLCA1NSwgMSwgMCwgMiwgNTcsIDEsIDAsIDIsIDU3LCAxLCAwLCAyLCA5NywgMSwgMCwgMiwgMTAxLCAxLCAwLCAyLCA1MCwgMSwgMCwgMiwgMTAwLCAxLCAwLCAyLCA1NywgMSwgMCwgMiwgNTcsIDEsIDAsIDIsIDQ4LCAxLCAwLCAyLCAxMDAsIDEsIDAsIDIsIDUxLCAxLCAwLCAyLCA1MSwgMSwgMCwgMiwgMTAwLCAxLCAwLCAyLCAxMDAsIDEsIDAsIDIsIDUxLCAxLCAwLCAyLCAxMjUsIDEsIDAsIDEwOSwgOTcsIDEwOCwgMTE5LCA5NywgMTE0LCAxMDEsIDMyLCAxMDUsIDExNSwgMzIsIDEwNSwgMTA4LCAxMDgsIDEwMSwgMTAzLCA5NywgMTA4LCAzMiwgOTcsIDExMCwgMTAwLCAzMiwgMTAyLCAxMTEsIDExNCwgMzIsIDExMCwgMTAxLCAxMTQsIDEwMCwgMTE1LCAxMCwgOTksIDk3LCAxMTYsIDExNSwgMzIsIDk3LCAxMTQsIDEwMSwgMzIsIDk5LCAxMTEsIDExMSwgMTA4LCAzMiwgOTcsIDExMCwgMTAwLCAzMiwgOTgsIDk3LCAxMDAsIDk3LCAxMTUsIDExNSwgMTAsIDEwMiwgMTA4LCA5NywgMTAzLCAxMjMsIDUxLCA1MywgMTAwLCA5OSwgOTgsIDk3LCA0OSwgNTEsIDQ4LCA1MSwgNTEsIDUyLCA1MywgNTcsIDk5LCA5NywgNTUsIDU3LCA1NywgOTcsIDEwMSwgNTAsIDEwMCwgNTcsIDU3LCA0OCwgMTAwLCA1MSwgNTEsIDEwMCwgMTAwLCA1MSwgMTI1&ieol=CRLF), but here’s a cleaned version: [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Decimal('Space',false)Decode_text('UTF-8%20(65001)')&input=MiwgMTA5LCAxLCAwLCAyLCA5NywgMSwgMCwgMiwgMTA4LCAxLCAwLCAyLCAxMTksIDEsIDAsIDIsIDk3LCAxLCAwLCAyLCAxMTQsIDEsIDAsIDIsIDEwMSwgMSwgMCwgMiwgMzIsIDEsIDAsIDIsIDEwNSwgMSwgMCwgMiwgMTE1LCAxLCAwLCAyLCAzMiwgMSwgMCwgMiwgMTA1LCAxLCAwLCAyLCAxMDgsIDEsIDAsIDIsIDEwOCwgMSwgMCwgMiwgMTAxLCAxLCAwLCAyLCAxMDMsIDEsIDAsIDIsIDk3LCAxLCAwLCAyLCAxMDgsIDEsIDAsIDIsIDMyLCAxLCAwLCAyLCA5NywgMSwgMCwgMiwgMTEwLCAxLCAwLCAyLCAxMDAsIDEsIDAsIDIsIDMyLCAxLCAwLCAyLCAxMDIsIDEsIDAsIDIsIDExMSwgMSwgMCwgMiwgMTE0LCAxLCAwLCAyLCAzMiwgMSwgMCwgMiwgMTEwLCAxLCAwLCAyLCAxMDEsIDEsIDAsIDIsIDExNCwgMSwgMCwgMiwgMTAwLCAxLCAwLCAyLCAxMTUsIDEsIDAsIDIsIDEwLCAxLCAwLCAyLCA5OSwgMSwgMCwgMiwgOTcsIDEsIDAsIDIsIDExNiwgMSwgMCwgMiwgMTE1LCAxLCAwLCAyLCAzMiwgMSwgMCwgMiwgOTcsIDEsIDAsIDIsIDExNCwgMSwgMCwgMiwgMTAxLCAxLCAwLCAyLCAzMiwgMSwgMCwgMiwgOTksIDEsIDAsIDIsIDExMSwgMSwgMCwgMiwgMTExLCAxLCAwLCAyLCAxMDgsIDEsIDAsIDIsIDMyLCAxLCAwLCAyLCA5NywgMSwgMCwgMiwgMTEwLCAxLCAwLCAyLCAxMDAsIDEsIDAsIDIsIDMyLCAxLCAwLCAyLCA5OCwgMSwgMCwgMiwgOTcsIDEsIDAsIDIsIDEwMCwgMSwgMCwgMiwgOTcsIDEsIDAsIDIsIDExNSwgMSwgMCwgMiwgMTE1LCAxLCAwLCAyLCAxMCwgMSwgMCwgMiwgMTAyLCAxLCAwLCAyLCAxMDgsIDEsIDAsIDIsIDk3LCAxLCAwLCAyLCAxMDMsIDEsIDAsIDIsIDEyMywgMSwgMCwgMiwgNTEsIDEsIDAsIDIsIDUzLCAxLCAwLCAyLCAxMDAsIDEsIDAsIDIsIDk5LCAxLCAwLCAyLCA5OCwgMSwgMCwgMiwgOTcsIDEsIDAsIDIsIDQ5LCAxLCAwLCAyLCA1MSwgMSwgMCwgMiwgNDgsIDEsIDAsIDIsIDUxLCAxLCAwLCAyLCA1MSwgMSwgMCwgMiwgNTIsIDEsIDAsIDIsIDUzLCAxLCAwLCAyLCA1NywgMSwgMCwgMiwgOTksIDEsIDAsIDIsIDk3LCAxLCAwLCAyLCA1NSwgMSwgMCwgMiwgNTcsIDEsIDAsIDIsIDU3LCAxLCAwLCAyLCA5NywgMSwgMCwgMiwgMTAxLCAxLCAwLCAyLCA1MCwgMSwgMCwgMiwgMTAwLCAxLCAwLCAyLCA1NywgMSwgMCwgMiwgNTcsIDEsIDAsIDIsIDQ4LCAxLCAwLCAyLCAxMDAsIDEsIDAsIDIsIDUxLCAxLCAwLCAyLCA1MSwgMSwgMCwgMiwgMTAwLCAxLCAwLCAyLCAxMDAsIDEsIDAsIDIsIDUxLCAxLCAwLCAyLCAxMjUsIDEsIDAsIDEwOSwgOTcsIDEwOCwgMTE5LCA5NywgMTE0LCAxMDEsIDMyLCAxMDUsIDExNSwgMzIsIDEwNSwgMTA4LCAxMDgsIDEwMSwgMTAzLCA5NywgMTA4LCAzMiwgOTcsIDExMCwgMTAwLCAzMiwgMTAyLCAxMTEsIDExNCwgMzIsIDExMCwgMTAxLCAxMTQsIDEwMCwgMTE1LCAxMCwgOTksIDk3LCAxMTYsIDExNSwgMzIsIDk3LCAxMTQsIDEwMSwgMzIsIDk5LCAxMTEsIDExMSwgMTA4LCAzMiwgOTcsIDExMCwgMTAwLCAzMiwgOTgsIDk3LCAxMDAsIDk3LCAxMTUsIDExNSwgMTAsIDEwMiwgMTA4LCA5NywgMTAzLCAxMjMsIDUxLCA1MywgMTAwLCA5OSwgOTgsIDk3LCA0OSwgNTEsIDQ4LCA1MSwgNTEsIDUyLCA1MywgNTcsIDk5LCA5NywgNTUsIDU3LCA1NywgOTcsIDEwMSwgNTAsIDEwMCwgNTcsIDU3LCA0OCwgMTAwLCA1MSwgNTEsIDEwMCwgMTAwLCA1MSwgMTI1&ieol=CRLF) to get the flag:

```
malware is illegal and for nerds
cats are cool and badass
flag{35dcba13033459ca799ae2d990d33dd3}
```

# Flag

- flag{35dcba13033459ca799ae2d990d33dd3}