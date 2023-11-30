#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    numb_args = len(argv) - 1
    args =  argv[1:]

    if numb_args == 0:
        print("0 arguments.")
    elif numb_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(numb_args))

    for i, arg in enumerate(args, 1):
        print("{}: {}".format(i, arg))

