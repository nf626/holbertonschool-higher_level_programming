#!/usr/bin/python3
"""Class to Json module"""
import json


def class_to_json(obj):
    """Change class to json function
        returns dictionary layout
    """
    return obj.__dict__
