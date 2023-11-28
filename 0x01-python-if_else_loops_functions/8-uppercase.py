#!/usr/bin/python3

def uppercase(str):
    for i in str:
        upper_char = i
        if ord("a") <= ord(i) <= ord("z"):
            upper_char = chr(ord(i) - 32)
        print("{:s}".format(upper_char), end="")
    print()
