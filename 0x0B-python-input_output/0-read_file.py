#!/usr/bin/python3

"""function that reads a text"""


def read_file(filename=""):
    """reads a text and prints it out to stout"""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end="")
