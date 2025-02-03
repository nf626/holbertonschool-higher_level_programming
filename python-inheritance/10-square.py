#!/usr/bin/python3
"""Geometry module"""
Rectangle = __import__('9-rectangle').Rectangle

class Rectangle(BaseGeometry):
    """Sub-class of BaseGeometry"""
    def __init__(self, width, height):
        """Initialise rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
