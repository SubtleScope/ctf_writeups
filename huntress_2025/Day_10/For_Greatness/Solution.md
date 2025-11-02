# Prompt

![](/huntress_2025/Day_10/For_Greatness/Challenge_ForGreatness.png "Challenge Prompt")

# Solution

- This one was fun and I got it pretty quickly which is nice. So you are given a zip file that contains a php file. View the file, there is a big chunk of data in it, so let’s print it using the php command line:

![Step 1](/huntress_2025/Day_10/For_Greatness/Step_1_PHP_Code.png "Step 1")

```
php -a
echo "BLOB";
```

![Step 2](/huntress_2025/Day_10/For_Greatness/Step_2_PHP_Shell.png "Step 2")

- Which is a huge chunk of base64. So I saved that to a file big_chunk.b64. I then dumped that to a new file and base64 decoded it.

```shell
base64 -d big_chunk.b64 > big_chunk.bin
file big_chunk.bin
sudo apt install qpdf
zlib-flate -uncompress < big_chunk.bin > big_chunk.1
```

- In big_chunk.1, there’s more base64 code. For this I used CyberChef.

![Step 3](/huntress_2025/Day_10/For_Greatness/Step_3_Base64.png "Step 3")

![Step 4](/huntress_2025/Day_10/For_Greatness/Step_4_CyberChef.png "Step 4")

- In this file, you wil see: 

```php
"..<ghost+}f7113307018770d52d4f94fec013197f{galf@greatness.com>";
```

![Step 5](/huntress_2025/Day_10/For_Greatness/Step_5_Reversed_Flag.png "Step 5")

- Here’s the [CyberChef](https://gchq.github.io/CyberChef/#recipe=Reverse('Character')&input=fWY3MTEzMzA3MDE4NzcwZDUyZDRmOTRmZWMwMTMxOTdme2dhbGY) link. Reverse the text and get the flag. Can also be done with this ChatGPT generated code (with help since I had already solved it)

```python
import re, base64, zlib, sys, os

IN_PATH = "j.php"
OUT_DECOMP = "decompressed_payload.php"
OUT_INNERS = "inner_decoded_candidates.txt"

def unescape_php_escapes(s: bytes) -> bytes:
    """Convert PHP-style escapes \\xHH and \\OOO (octal) in a bytes string to raw bytes."""
    text = s.decode('utf-8', errors='ignore')
    # First handle \xHH
    def repl_x(m):
        hh = m.group(1)
        return chr(int(hh, 16))
    text = re.sub(r'\\x([0-9A-Fa-f]{2})', lambda m: repl_x(m), text)
    # Then handle octal \NNN (1-3 digits)
    def repl_o(m):
        octs = m.group(1)
        try:
            return chr(int(octs, 8))
        except Exception:
            return ''
    text = re.sub(r'\\([0-7]{1,3})', lambda m: repl_o(m), text)
    return text.encode('utf-8', errors='ignore')

def find_largest_base64_blob(text: str, min_len: int = 200) -> str:
    # Find long base64-like sequences (A-Za-z0-9+/ with optional padding). Return the longest that passes earliest checks.
    candidates = re.findall(r'([A-Za-z0-9+/]{%d,}={0,2})' % min_len, text)
    if not candidates:
        return None
    # Return the longest candidate
    return max(candidates, key=len)

def try_base64_decode(s: str):
    try:
        return base64.b64decode(s, validate=True)
    except Exception:
        # try with padding fix
        pad = len(s) % 4
        if pad:
            s2 = s + ("=" * (4 - pad))
            try:
                return base64.b64decode(s2, validate=False)
            except Exception:
                return None
        return None

def find_inner_base64_chunks(text: str, min_len=40, max_len=2000):
    # Find base64-like substrings inside the decompressed payload
    cand = []
    for m in re.finditer(r'([A-Za-z0-9+/]{%d,%d}={0,2})' % (min_len, max_len), text):
        s = m.group(1)
        # exclude very repetitive short patterns
        cand.append((m.start(), s))
    return cand

def search_reversed_flag(decoded_text: str):
    # Look for patterns where the flag appears reversed: e.g. "}...{galf" or "galf...{"
    # We'll search for 'galf' and then grab surrounding chars that include braces
    results = []
    # pattern like "}...galf" (closing brace then stuff then 'galf')
    for m in re.finditer(r'\}[^}{]{1,300}galf', decoded_text):
        frag = m.group(0)
        results.append(frag[::-1])  # reverse
    # pattern like 'galf...{'
    for m in re.finditer(r'galf[^}{]{1,300}\{', decoded_text):
        frag = m.group(0)
        results.append(frag[::-1])
    # Also try searching for 'galf' occurrences and reverse a window around them
    if not results:
        for m in re.finditer(r'galf', decoded_text):
            i = m.start()
            # take 200 chars before and after and reverse
            start = max(0, i-200)
            end = min(len(decoded_text), i+200)
            window = decoded_text[start:end]
            rev = window[::-1]
            if 'flag{' in rev:
                # extract the flag token from rev
                ff = re.search(r'flag\{[^\}]{1,500}\}', rev)
                if ff:
                    results.append(ff.group(0))
    return results

def main():
    if not os.path.exists(IN_PATH):
        print("Input file not found:", IN_PATH)
        return 1
    raw = open(IN_PATH, "rb").read()
    print("[*] Read %d bytes from %s" % (len(raw), IN_PATH))

    # Unescape sequences
    unescaped = unescape_php_escapes(raw)
    print("[*] After unescape size:", len(unescaped))
    text = unescaped.decode('utf-8', errors='ignore')

    # Find largest base64 blob
    bigb64 = find_largest_base64_blob(text, min_len=200)
    if not bigb64:
        print("[!] No large base64 blob found in unescaped text")
        # As fallback, treat entire file as possible base64 blob
        bigb64 = None
    else:
        print("[*] Found base64 blob of length", len(bigb64))

    decoded = None
    if bigb64:
        decoded = try_base64_decode(bigb64)
        if decoded is None:
            print("[!] base64 decode failed for the found blob")
        else:
            print("[*] base64 decoded blob size:", len(decoded))
    else:
        # attempt to detect any base64 in the raw file
        possible = re.search(rb'([A-Za-z0-9+/]{200,}={0,2})', raw)
        if possible:
            bigb64 = possible.group(1).decode('utf-8', errors='ignore')
            decoded = try_base64_decode(bigb64)
            print("[*] Found large base64 in raw binary, decoded? ", decoded is not None)

    # Try zlib decompress if decoded present
    decomp = None
    if decoded:
        try:
            decomp = zlib.decompress(decoded)
            print("[*] zlib decompressed size:", len(decomp))
            open(OUT_DECOMP, "wb").write(decomp)
            print("[*] Wrote decompressed payload to", OUT_DECOMP)
        except Exception as e:
            print("[!] zlib.decompress failed:", e)
            # try gzip?
            try:
                import gzip, io
                decomp = gzip.decompress(decoded)
                print("[*] gzip decompressed size:", len(decomp))
                open(OUT_DECOMP, "wb").write(decomp)
            except Exception as e2:
                print("[!] gzip decompression also failed:", e2)

    if not decomp:
        print("[!] No decompressed payload to inspect further. Exiting.")
        return 1

    dec_text = decomp.decode('utf-8', errors='ignore')

    # Find inner base64 chunks within the decompressed text
    inner = find_inner_base64_chunks(dec_text, min_len=40, max_len=2000)
    print("[*] Found %d inner base64-like candidates in decompressed payload" % len(inner))

    found_flags = []
    with open(OUT_INNERS, "w", encoding="utf-8") as outf:
        for idx, (pos, b64s) in enumerate(inner):
            # attempt decode
            data = try_base64_decode(b64s)
            if data:
                # write a note
                outf.write("=== candidate %d pos=%d len=%d ===\n" % (idx, pos, len(b64s)))
                outf.write(b64s + "\n\n")
                try:
                    # try further decompression if seems compressed
                    try:
                        txt = zlib.decompress(data).decode('utf-8', errors='ignore')
                        outf.write("[zlib-decompressed inner]\n")
                        outf.write(txt + "\n\n")
                    except Exception:
                        txt = data.decode('utf-8', errors='ignore')
                        outf.write("[decoded inner as text]\n")
                        outf.write(txt + "\n\n")
                except Exception as e:
                    outf.write("[could not decode inner to text] %s\n\n" % e)
                # search for reversed flag patterns in the decoded inner text
                search_text = txt if isinstance(txt, str) else ""
                results = search_reversed_flag(search_text)
                if results:
                    for r in results:
                        # r may already be reversed into normal orientation if we returned reversed earlier
                        if 'flag{' in r:
                            found_flags.append(r)
                        else:
                            # if r doesn't contain 'flag{' after reversing, try to reverse the original snippet
                            found_flags.append(r)
    if os.path.exists(OUT_INNERS):
        print("[*] Wrote inner decoded candidates to", OUT_INNERS)

    # As a last pass, also directly search decompressed text for reversed flag fragments without relying on inner base64 extraction
    direct_results = search_reversed_flag(dec_text)
    if direct_results:
        for dr in direct_results:
            if 'flag{' in dr:
                found_flags.append(dr)
            else:
                found_flags.append(dr)

    # Deduplicate and print findings
    uniq = []
    for f in found_flags:
        if f not in uniq:
            uniq.append(f)
    if uniq:
        print("\n[+] Found possible flag-like strings (reversed or corrected):")
        for u in uniq:
            print(u)
    else:
        print("\n[!] No reversed flag patterns found in inner decoded blobs or decompressed text.")

    return 0

if __name__ == "__main__":
    sys.exit(main())
```



# Flag

- flag{f791310cef49f4d25d0778107033117f}