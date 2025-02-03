#!/usr/bin/python3
"""Module: Check if object is sub-class"""


def inherits_from(obj, a_class):
    """Function to check if object is sub-class"""
    return (isinstance(obj, a_class) and type(obj) is not a_class)
