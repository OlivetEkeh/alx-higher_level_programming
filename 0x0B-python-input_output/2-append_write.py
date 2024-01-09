#!/usr/bin/python3

"""function that appends a string"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file"""

    with open(filename, 'a', encoding='utf-8') as file:
        nb_characters_added = file.write(text)
        return nb_characters_added
