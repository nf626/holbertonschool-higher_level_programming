#!/usr/bin/python3
"""Create object from Json module"""
import json


def load_from_json_file(filename):
    """Load from json function"""
    with open(filename) as load_file:
        load_file = json.load(filename)
        return load_file
