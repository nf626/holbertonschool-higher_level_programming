#!/usr/bin/python3
"""Create object from Json module"""
import json


def load_from_json_file(filename):
    """Load from json function"""
    with open(filename, encoding="utf-8") as load_file:
        new_obj = json.load(load_file)
        return new_obj
