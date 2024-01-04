#!/usr/bin/python3
"""
a function that prints a text with 2 new lines after each of these characters: ., ? and :
"""

def text_indentation(text):
    """
    Print the text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sentences = text.split('.') + text.split('?') + text.split(':')

    for sentence in sentences:
        print(sentence.strip())
        if sentence != sentences[-1]:
            print("\n")
 
