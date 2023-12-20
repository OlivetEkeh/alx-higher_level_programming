#!/usr/bin/python3

"""This is the square class"""


class Square:
    """Square class that defines a square by: (based on 1-square.py)"""
    def __init__(self, size=0):
        """Initializer for the Square class.

        Args:
            size (int, optional): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    @property
    def size(self):
        """Getter method to retrieve the value of attribute `size`."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the value of the private attribute `size`.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value
