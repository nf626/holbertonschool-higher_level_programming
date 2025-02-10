#!/usr/bin/python3
"""Object to Json module"""
import json

def to_json_string(my_obj):
    """json function"""
    json_string = json.dumps(my_obj)
    return json_string
