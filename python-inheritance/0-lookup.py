#!/usr/bin/python3
""" function that returns the list of
    available attributes and methods of an object"""


def lookup(obj):
    """function returns list of
        attributes and methods"""
    return dir(obj)
