#!/usr/bin/python3

""" My List """


class MyList(list):
    """A class that inherits from list 
    with an additional method."""


    def print_sorted(self):
        print(sorted(self))
