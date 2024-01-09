#!/usr/bin/python3

"""writes a string to a text file"""


def write_file(filename="", text=""):
    """writes a string to text"""

    with open(filename, 'w', encoding='utf-8') as file:
        nb_characters = file.write(text)
        return nb_characters
