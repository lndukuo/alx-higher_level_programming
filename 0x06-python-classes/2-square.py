#!/usr/bin/python3

"""Define class Square."""


class Square:
    """Rep a square."""

    def __init__(self, size=0):
        """Init a new square.
        args:
            size (init): size of the new square."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size
