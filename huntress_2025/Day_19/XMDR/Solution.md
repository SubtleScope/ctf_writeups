# Prompt

![](/huntress_2025/Day_19/XMDR/Challenge_XMDR.png "Challenge Prompt")

# Solution

- Okay, so I started looking at all of things and doing typical forensics. Some things didn’t work due to not existing or permissions issues. I found the actual GTRS file early on and had the code, but didn’t take a look at Chrome or research GTRS - doh!. Though I did look at Internet Explorer and some Chrome things (albeit the wrong ones, lol). So below will show the direct path to getting the flag. I also did fall into a little bit of the trap of Baby Shark for a little 

- If we look at the user’s downloads from the hint on the side of the page, we can see that the GTRS exists in the Downloads.

![Alerts](/huntress_2025/Day_19/XMDR/MDR_Alert.png "Alerts")

![GTRS](/huntress_2025/Day_19/XMDR/GTRS.png "GTRS")

- Download that and take a look at what it does. We can see that it does stuff with Google Translate, so this is a big hint it is dealing with web stuff. Through some of the other searches, I saw Google Chrome being used and was in the mix. So if we grab the Google History database, we can grab data from it. 

![Chrome History](/huntress_2025/Day_19/XMDR/Google_Data.png "Chrome History")

- Here we can see an assortment of Google Translate links using (DB Browser for SQLite). Extract them to a text file. NOTE: I forgot, this was a .json file that I modified. The code below only works for reading each url on a new line. So you may want to modify it to support JSON or do I what I did. 

![SQLite Browser](/huntress_2025/Day_19/XMDR/DB_Browser.png "SQLite Browser")

- Now that we have the links, we can build a decoder for the urls and see if one contains the flag. Here’s an example of a url decoded within CyberChef:

![Cyber Chef - URL](/huntress_2025/Day_19/XMDR/CyberChef.png)

- Run the script below with the urls.txt you saved from the database. `python process_urls.py urls.txt`

```python
#!/usr/bin/env python3
import re, sys, io, binascii
from urllib.parse import urlparse, parse_qs, unquote_plus

def get_text_param(url: str) -> str:
    try:
        q = parse_qs(urlparse(url).query)
        raw = q.get('text', [''])[0]
        return unquote_plus(raw)
    except Exception:
        return ''

def iter_command_blocks(s: str):
    # grab everything between the markers, including newlines
    for m in re.finditer(r'STARTCOMMAND\s*(.*?)\s*ENDCOMMAND', s, re.S):
        yield m.group(1).strip()

def uu_decode_block(block: str) -> bytes:
    """
    Accepts either full uuencoded file blocks:
        begin 664 -\n<uu-lines>\nend
    or just raw uuencoded lines (rare). Returns decoded bytes.
    """
    # normalize newlines
    lines = [ln.rstrip('\r') for ln in block.splitlines() if ln.strip() != '']
    if not lines:
        return b''

    # If it has a 'begin'...'end' wrapper, strip it; keep only uu lines.
    if lines[0].lower().startswith('begin ') and lines[-1].lower() == 'end':
        lines = lines[1:-1]

    # Some operators put a lone backtick ` line as uu terminator; keep it.
    out = io.BytesIO()
    for ln in lines:
        try:
            # Each uu line decodes independently
            out.write(binascii.a2b_uu(ln.encode('ascii', 'ignore')))
        except binascii.Error:
            # not a uu line; ignore harmless junk
            pass
    return out.getvalue()

def decode_from_urls(urls):
    for url in urls:
        text = get_text_param(url)
        if not text:
            continue
        for i, blk in enumerate(iter_command_blocks(text), 1):
            decoded = uu_decode_block(blk)
            if decoded:
                try:
                    print(f'\n[URL] {url}\n[BLOCK #{i}]')
                    print(decoded.decode('utf-8', 'replace'))
                except UnicodeDecodeError:
                    print(f'\n[URL] {url}\n[BLOCK #{i}] (binary)')
                    print(decoded)
            else:
                # If uu failed, show the raw block as a fallback
                print(f'\n[URL] {url}\n[BLOCK #{i}] (raw)')
                print(blk)

if __name__ == "__main__":
    # usage:
    #   python decode_translate_c2.py urls.txt
    # or paste URLs via stdin
    data = []
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8', errors='ignore') as f:
            data = [ln.strip() for ln in f if ln.strip()]
    else:
        data = [ln.strip() for ln in sys.stdin if ln.strip()]
    decode_from_urls(data)
```

!["Solution"](/huntress_2025/Day_19/XMDR/Flag.png "Solution")

# Flag

- flag{69200c13dcb39de19a405e9d1f993821}