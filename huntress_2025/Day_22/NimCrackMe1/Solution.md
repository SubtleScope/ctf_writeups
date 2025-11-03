# Prompt

![](/huntress_2025/Day_22/NimCrackMe1/Challenge_NimCrackMe1.png "Challenge Prompt")

# Solution

- I threw the program in IDA and identified some of the functions by name. 

![Function Names](/huntress_2025/Day_22/NimCrackMe1/Function_Names.png "Function Names")

- So I ran through the program and set a breakpoint in that function at the end where the value is returned: 

![XOR Function](/huntress_2025/Day_22/NimCrackMe1/XOR_Function.png "XOR Function")

![Breakpoints](/huntress_2025/Day_22/NimCrackMe1/Breakpoints.png "Breakpoints")

- At this point, looking through the registers, we can easily identify the flag in the executable, dump it, and then submit it. 

![Flag](/huntress_2025/Day_22/NimCrackMe1/Flag.png "Flag")

# Flag

- flag{852ff73f9be462962d949d563743b86d}