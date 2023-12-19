#!/usr/bin/python3

"""Define class square with private instance attribute size."""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Initialization of a new class with a given size.

        Parameters:
        - size (int): size of the square (default = 0).
        """
        self.__size = size
