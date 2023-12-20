#!/usr/bin/python3

"""
    This is the Square class.
    """

class Square:

    def __init__(self, size=0):
        """
        This is the constructor for the Square class.

        Parameters:
        - size (int, optional): The size of the square. Default is 0.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
