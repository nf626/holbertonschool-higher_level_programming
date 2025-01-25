#!/usr/bin/python3
"""Module: Add integers"""

def add_integer(a, b=98):
    """function adds two integers"""
    total = 0
    try:
        total = int(a) + int(b)
    except (TypeError, ValueError):
        print("b must be an integer")
        print("a must be an integer")
    finally:
        return total
