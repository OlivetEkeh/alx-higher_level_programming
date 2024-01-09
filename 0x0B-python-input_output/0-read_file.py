#!/usr/bin/python3

"""function that reads a text"""


def read_file(filename=""):
    """reads a text"""

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end="")
