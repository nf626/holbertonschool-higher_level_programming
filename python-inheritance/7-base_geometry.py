#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    """Geometry class"""

    def area(self):
        """Area instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
