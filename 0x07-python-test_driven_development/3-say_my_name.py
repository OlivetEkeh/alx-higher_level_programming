#!/usr/bin/python3
""" Prints out a given string """

def say_my_name(first_name, last_name=""):
    """ Prints out first and last name """
    if type(first_name) is not a str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not a str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}") 
