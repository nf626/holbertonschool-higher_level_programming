#!/usr/bin/python3
"""Access and update private attribute"""


class Square:
    """Class to create square"""
    __size = None

    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """getter method"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter method"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate area"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints a square"""
        if self.__size == 0:
            print("")

        for i in range(self.__size):
            print("#" * self.__size)
