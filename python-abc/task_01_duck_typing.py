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
        self.radius = radius

    def area(self):
        """Area method"""
        return (math.pi * (self.radius ** 2))
    
    def perimeter(self):
        """Perimeter method"""
        return (2 * math.pi * self.radius)

class Rectangle(Shape):
    """Rectangle class"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Area method"""
        return (self.width * self.height)
    
    def perimeter(self):
        """Perimeter method"""
        return ((self.width * 2) + (self.height * 2))


def shape_info(shape_var):
    """Shape info function"""
    print(f"Area: {shape_var.area()}")
    print(f"Perimeter: {shape_var.area()}")
