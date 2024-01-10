#!/usr/bin/python3
"""Defines a function to write files."""


def write_file(filename="", text=""):
    """Write a string to a UTF* text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to be written.
    Return:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
