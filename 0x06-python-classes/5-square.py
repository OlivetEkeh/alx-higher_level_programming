#!/usr/bin/python3

class Square:
    """
    This is the Square class.
    """
    def __init__(self, size=0):
        """
        This is the constructor for the Square class.

        Parameters:
        - size (int, optional): The size of the square. Default is 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size.

        Returns:
        - int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size.

        Parameters:
        - value (int): The size to set.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Public instance method to calculate and return the current square area.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Public instance method to print the square with the character #.

        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
