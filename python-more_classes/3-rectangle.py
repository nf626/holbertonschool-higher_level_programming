#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Rectangle Class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """access width data"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """access height data"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area"""
        return self.width * self.height

    def perimeter(self):
        """perimeter"""
        if (self.width == 0 or self.height == 0):
            return int(0)
        return (self.width * 2 + self.height * 2)

    def print_str(self):
        if (self.width == 0 or self.height == 0):
            print("")
        for i in self.height:
            print("#" * (self.height + self.width))
