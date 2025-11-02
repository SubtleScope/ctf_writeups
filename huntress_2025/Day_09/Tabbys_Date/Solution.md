# Prompt

![](/huntress_2025/Day_09/Tabbys_Date/Challenge_TabbysDate.png "Challenge Prompt")

# Solution

```
7z -x tabbys_date.zip
cd C
find . -name *.*
cd ./Users/Tabby/AppData/Local/Packages/Microsoft.WindowsNotepad_8wekyb3d8bbwe/LocalState/TabState/
ls -laS
file 2e0dd6b6-ba93-4efc-9fd4-985dad74869a.bin
less 2e0dd6b6-ba93-4efc-9fd4-985dad74869a.bin
```

![Step 1](/huntress_2025/Day_09/Tabbys_Date/Step_1_find.png "Step 1")

![Step 2](/huntress_2025/Day_09/Tabbys_Date/Step_2_ls.png "Step 2")

```
xxd 2e0dd6b6-ba93-4efc-9fd4-985dad74869a.bin | awk -F" " '{ print $10 $11 }' | tr -d '.' | grep -A 4 flag | tr -d '\n'
```

![Step 3](/huntress_2025/Day_09/Tabbys_Date/Step_3_xxd.png "Step 3")

# Flag

- flag{165d19b610c02b283fc1a6b4a54c4a58}