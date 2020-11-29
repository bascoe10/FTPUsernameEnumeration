# FTP USERNAME Enumeration

Single threaded python script for FTP users enumeration.
Usernames are printed as found. No output if no user is found.

Useful for penetration testing

## Usage
```nashorn js
kali@kali:~/$ python3 ftpuserenum.py 10.10.10.197 users.txt
developer --> found
```

Port defaults to 21 but can be changed with the `-p` or `--port`
## TODO
- Handle socket exceptions more gracefully
- Make multi threaded