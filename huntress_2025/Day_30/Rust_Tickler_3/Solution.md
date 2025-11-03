# Prompt

![](/huntress_2025/Day_30/Rust_Tickler_3/Challenge_RustTickler3.png "Challenge Prompt")

# Solution

## Part 1

- For the first part, it is similar to the rust2 payload, except the values are different. Essentially, you can do the same thing where you change the value of r8d to the seed value and then come away with the various strings. It was a little bit of a process, but you can find the location where the seeds are loaded and the corresponding strings. Not all of them are called within the program itself. Below is a memory dump of the process where the lookup table is located. I can’t remember how I initially found it, but it was in one of the functions where it actually loads. It might be this one: sub_7FF7BBB6D890.

![Table Mapping](/huntress_2025/Day_30/Rust_Tickler_3/Table_Map.png "Table Mapping")

- Working through the code and entering the various values, you can build out a table of the values with some hints to the challenge. Not included in the table is the pointer to the memory address, but it does include the size, seed, and decoded/decrypted string value.

| Size | Seed (little endian) | Seed (big endian) | String                                               |
|:-----|:---------------------|:------------------|:-----------------------------------------------------|
0x20   | 0x3713               | 0x1337            | "What is my favorite sha256 hash?"                   |
0x32   | 0x4013 	          | 0x1340 	          | "These are practically the same red herring strings" |
0x7	   | 0x4913 	          | 0x1349 	          | "APPDATA"	                                         |
0x20   | 0x4213	              | 0x1342 	          | "Reality is soup and I AM A FORK!"                   |
0x31   | 0x3E13 	          | 0x133E 	          | "The flag is the hash of the name of a certain cat"  |
0x2C   | 0x3813 	          | 0x1338 	          | "Wrong, that's not my favorite sha256 hash..."       |
0x19   | 0x3F13 	          | 0x133F 	          | "Follow the Gray Rabbit..."                          |
0x4	   | 0x6A13 	          | 0x136A 	          | ".txt"	                                             |
0x40   | 0x3A13 	          | 0x133A 	          | a4ec6d39192922bdec0e310db3dda25f21f1d7e8e9e68cfebc156553e4123b03 |
0x1F   | 0x3B13 	          | 0x133B 	          | "Crab tickler 2! Rust RE is fun!"                    |
0x1D   | 0x4313 	          | 0x1343 	          | "I am totally a purple herring"                      |
0x1A   | 0x6913 	          | 0x1369 	          | "rust-tickler-3-stage-2.exe"                         |
0x27   | 0x3C13 	          | 0x133C 	          | "You are going to find the flag in here?"            |
0x6	   | 0x4813 	          | 0x1348 	          | "Exodus"                                             |
0x15   | 0x3D13 	          | 0x133D 	          | "The flag is not here!"                              |
0x39   | 0x3913 	          | 0x1339 	          | "Thank you, Bingus! But our princess is in another castle!" |

- So if you enter the hash into the program, you get: 

![Program Input](/huntress_2025/Day_30/Rust_Tickler_3/Program_Input.png "Program Input")

- Noticeably missing, if you solved this, is the 0x1341 in the table, which, if you set r8d to that value, will crash the program. What it does is loads a byte stream that is XOR encoded by the highlighted favorite hash. The size is 0x001452 or 0x521400.

![Entry Size](/huntress_2025/Day_30/Rust_Tickler_3/Table_Entry_Size.png "Entry Size")

- You then select those bytes based on the memory address pointed to by the table mapping. You can do this in IDA, but I chose Malcat instead. 

![Entry Selection](/huntress_2025/Day_30/Rust_Tickler_3/Entry_Selection.png "Entry Selection")

- Take this value and XOR it using your favorite program and you’ll get a whole new binary. 

![Exported/Encrypted Selection](/huntress_2025/Day_30/Rust_Tickler_3/Exported_Selection.png "Exported/Encrypted Selection")

![Decrypted Selection](/huntress_2025/Day_30/Rust_Tickler_3/Decrypted_Selection.png "Decrypted Selection")

## Part 2

- Now analyze the new program. The program takes your input (I found as long as it matches the length of a valid flag), encrypts it, and then compares that to the encrypted flag value. So you need to go through the program to the point where it compares the encrypted data, so you can decrypt the flag bytes.

```
v84 = &unk_7FF6D717D128; // The Key pointer structure 
v85 = 32LL; // Key length (32 bytes) 
v86 = &unk_7FF6D717D148; // This pointer structure
v87 = 16LL; //IV length (16 bytes)

Values: 

Key: D4C39486FDF04283F5D96436BA68EA1C4F4194796AF82D0F8EED7C12F53FA07C
IV: 539FB31E1CC13442420D039397E91777
```

- In function sub_7FF6D6E01E30, you will find the line: `if ( memcmp(Buf1, (const void *)(v23 + v17), v12) )`. If you breakpoint that line and analyze v23, you will find the buffer containing the encrypted bytes of the flag. 

![Encrypted Flag Bytes](/huntress_2025/Day_30/Rust_Tickler_3/Encrypted_Flag.png "Encrypted Flag Bytes")

- Plug that into anything (Python) and decrypt the encrypted bytes.

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii

hex_ciphertext = "CB584B62035D138F77BC9810F00F1A2020700F8FBF0D75DCA3FD71085F1467CDE9D05F1F83BBC76B7D9BEB42F7510095"
hex_key_data = "D4C39486FDF04283F5D96436BA68EA1C4F4194796AF82D0F8EED7C12F53FA07C"
hex_iv = "539FB31E1CC13442420D039397E91777"

'''
[Attempting Decryption: AES-256-CBC]
  [+] SUCCESS! Decryption complete.
  Decrypted (hex): 666c61677b66623864653634316633383331353132323238343564396239393161313763327d
  Decrypted (text): flag{fb8de641f383151222845d9b991a17c2}
'''

try:
    ciphertext = bytes.fromhex(hex_ciphertext)
    
    hex_key = bytes.fromhex(hex_key_data)
    hex_iv = bytes.fromhex(hex_iv)

except (binascii.Error, ValueError) as e:
    print(f"Error converting hex string: {e}")
    print("Please double-check the hex strings for errors or odd lengths.")
    exit()

def attempt_decrypt(key, iv, mode, mode_name, nonce_len=8):
    try:
        print("-" * 40)
        print(f"[Attempting Decryption: {mode_name}]")
        
        cipher = None
        if mode == AES.MODE_CBC:
            cipher = AES.new(key, mode, iv)
    
        decrypted = cipher.decrypt(ciphertext)
        
        if mode == AES.MODE_CBC:
            try:
                decrypted = unpad(decrypted, AES.block_size)
            except ValueError as e:
                print(f"  [-] Unpadding FAILED: {e}")
                print("  (This is the expected error for a wrong key in CBC mode.)")
                print(f"  Raw decrypted (hex): {decrypted.hex()}")
                return False
        
        print(f"  [+] SUCCESS! Decryption complete.")
        print(f"  Decrypted (hex): {decrypted.hex()}")
        
        try:
            db = decrypted.rstrip(b'\x00').decode('utf-8')
            print(f"  Decrypted (text): {db}")
        except UnicodeDecodeError:
            print(f"  Decrypted (raw): {decrypted!r}")
            print("  (Could not decode as UTF-8, showing raw bytes)")
        return True
            
    except Exception as e:
        print(f"  [-] FAILED: {e}")
        return False

attempt_decrypt(hex_key, hex_iv, AES.MODE_CBC, "AES-256-CBC")
```

![Decrypted Flag](/huntress_2025/Day_30/Rust_Tickler_3/Decrypted_Flag.png "Decrypted Flag")

# Flag

- flag{fb8de641f383151222845d9b991a17c2}