#!/usr/bin/env python3
"""Shape Module"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Shape class"""
    @abstractmethod
    def area(self):
        """Default area"""
        raise NotImplementedError("area() must be implemented")

    @abstractmethod
    def perimeter(self):
        """Default perimeter"""
        raise NotImplementedError("perimeter() must be implemented")

class Circle(Shape):
    """Circle class"""
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        """Area method"""
        area_calc = math.pi * (self.__radius ** 2)
        if area_calc < 0:
            raise AssertionError("Area should handle negative radius")
        else:
            return area_calc

    def perimeter(self):
        """Perimeter method"""
        perimeter_calc = 2 * math.pi * self.__radius
        if perimeter_calc < 0:
            raise AssertionError("Perimeter should handle negative radius")
        else:
            return perimeter_calc

class Rectangle(Shape):
    """Rectangle class"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        """Area method"""
        return (self.__width * self.__height)
    
    def perimeter(self):
        """Perimeter method"""
        return ((self.__width * 2) + (self.__height * 2))

def shape_info(shape_var):
    """Shape info function"""
    print(f"Area: {shape_var.area()}")
    print(f"Perimeter: {shape_var.perimeter()}")
