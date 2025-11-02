# Prompt

![](/huntress_2025/Day_13/I_Forgot/Challenge_IForgot.png "Challenge Prompt")

# Solution

- I just started off by doing some general searching at first and found a couple of Notepad and a powershell process among others. There was an HTA file executed, but this turned out to not be related I believe. I did a bunch of other searches, there’s a lot of detection and unrelated crap, so you have to wade through it.

![Step 1](/huntress_2025/Day_13/I_Forgot/Step_1_Powershell.png "Step 1")

- Given that this is related to ransomware, I figured there would probably be some sort of instruction document. In my various searches, I found some steps for decrypting a key and also a possible zip file. 

![Instructions 1](/huntress_2025/Day_13/I_Forgot/Decrypt_Strings_1.png "Instructions 1")

![Instructions 2](/huntress_2025/Day_13/I_Forgot/Decrypt_Strings_2.png "Instructions 2")

- I used volatility to dump some of the processes, but the one we care about is PID: 2132

```shell
vol -f memdump.dmp windows.psscan.PsScan
vol -f memdump.dmp windows.pslist.PsList 
vol -f memdump.dmp -o ./dumps windows.memmap.Memmap --pid 2132 --dump
```

- When analyzed in Malcat, we can see that the decryption keys zip is located in the memory dump. We can also find a string with the password for decrypting the zip file. In the memory dump, we can find the malicious zip as well.  

![Malcat - Zip Password](/huntress_2025/Day_13/I_Forgot/Malcat_1.png "Malcat - Zip Password")

![Malcat - Byte View](/huntress_2025/Day_13/I_Forgot/Malcat_2.png "Malcat - Byte View")

- We can also see some possible decryption instructions. These can also be found by dumping the Notepad processes. 

```bash
vol -f memdump.dmp -o ./dumps windows.memmap.Memmap --pid 1388 --dump
vol -f memdump.dmp -o ./dumps windows.memmap.Memmap --pid 1628 --dump

grep -A 5 -ai 'ePDaACdOCwaMiYDG' dumps/pid.1388.dmp
grep -A 5 -ai 'ePDaACdOCwaMiYDG' dumps/pid.1628.dmp
```

- From here, we can see the steps and then start to reproduce them. We have the zip that we can unzip and then decrypt the key. 

```bash
grep -A 5 -ai 'openssl pkeyutl' memdump.dmp

# openssl pkeyutl -�0-in��)0-in<�.enc -out opt rsa_padding_mode:oaepl�(This writes<�: first 32 by=�� (hex), next 16jIV)
# Utilize the steps extracted from the memory dump
```

![Key Grep](/huntress_2025/Day_13/I_Forgot/Keyhex_Grep.png "Key Grep")

```shell
mkdir DECRYPT && cd DECRYPT
7z x ~/Downloads/decrypt.zip # enter password
openssl pkeyutl -decrypt -inkey private.pem -in key.enc -out key_raw.bin -pkeyopt rsa_padding_mode:oaep

# This outputs the memory dump strings which are not 100% exact
grep -a 'KEYHEX' ../memdump.dmp

# KEYHEX=$(xxd -p -c 256rp | head▒064)
# }/IV3@tail3!323
# �d -aes-256-cbc+{,�txt -K $�a -iv $zT

# Rebuild the command as best as we can
KEYHEX=$(xxd -p -c 256 key_raw.bin | head -c 64)
IV=$(xxd -p -c 256 key_raw.bin | head -c 96 | tail -c 32)

openssl enc -d -aes-256-cbc -in flag.enc -K "$KEYHEX" -iv "$IV" -out flag.txt
cat flag.txt
```
![Solution](/huntress_2025/Day_13/I_Forgot/Solution.png "Solution")

# Flag

- flag{fa838fa9823e5d612b25001740faca31}