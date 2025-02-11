#!/usr/bin/python3
"""Json to object module"""
import json


def from_json_string(my_str):
    """json to object function"""
    python_object = json.loads(my_str)
    return python_object
