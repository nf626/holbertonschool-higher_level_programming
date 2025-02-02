#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Rectangle Class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

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
        if (self.__width == 0 or self.__height == 0):
            return int(0)
        return (self.__width * 2 + self.__height * 2)

    def __str__(self) -> str:
        """Return string representation of rectangle"""
        if (self.width == 0 or self.height == 0):
            return ("")
        rectangle = ""
        for coloumn in range(self.__height):
            for row in range(self.__width):
                rectangle = rectangle + '#'
            if coloumn < self.__height - 1:
                rectangle = rectangle + '\n'
        return rectangle

    def __repr__(self):
        """Return a printable representation of rectangle"""
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
