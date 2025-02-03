#!/usr/bin/python3
"""Check if same object module"""


def is_same_class(obj, a_class):
    """Function returns True if object
        is exact copy of instance"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
