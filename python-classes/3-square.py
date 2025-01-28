#!/usr/bin/python3
"""Area of a square"""


class Square:
    """Class to create square"""
    __size = None

    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculate area"""
        return (self.__size ** 2)
