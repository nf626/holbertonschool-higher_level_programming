#!/usr/bin/python3
"""Access and update private attribute"""


class Square:
    """Class to create square"""
    __size = None

    def __init__(self, size=0):
        self.__size = size

    def size(self):
        """getter method"""
        return (self)
    
    def size(self, value):
        """setter method"""
        self.size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculate area"""
        return (self.__size ** 2)
