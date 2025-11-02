# Prompt

![](/huntress_2025/Day_04/Snooze/Challenge_Snooze.png "Challenge Prompt")

# Solution

```bash
file snooze
# snooze: compress'd data 16 bits
mv snooze snooze.z
uncompress -d ./snooze.z
file snooze
# snooze: ASCII text
cat snooze
# flag{c1c07c90efa59876a97c44c2b175903e}
```
# Flag

- flag{c1c07c90efa59876a97c44c2b175903e}