#!/usr/bin/python3
"""Module: Add two integers"""

def add_integer(a, b=98):
    """
    
    - Function adds two integers.
    - Raise a TypeError exception if a and b not integer or float
    - Returns an integer: the addition of a and b
    """
    total = 0
    if (not isinstance(a, float) and not isinstance(a, int)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, float) and not isinstance(b, int)):
        raise TypeError("b must be an integer")
    total = int(a) + int(b)
    return total
