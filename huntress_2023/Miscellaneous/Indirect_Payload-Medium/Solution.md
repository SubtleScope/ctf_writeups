# Prompt

![Challenge Prompt](Challenge.png "Challenge Prompt")

# Solution

- You are presented with a website that, when you press ‘Retrieve the Payload’, it redirects you a bunch of times. I tried with curl/wget, but they never seemed to be able to obtain the payload in response headers.

![Retrieving](Retrieving.png "Retrieving")

![Headers](Headers.png "Headers")

- Use Invoke-WebRequest to make the request and retrieve the flag from the payload.

![Solution](Solution.png "Solution")

flag{448c05ab3e3a7d68e3509eb85e87206f}