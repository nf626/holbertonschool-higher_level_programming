#!/usr/bin/python3
"""Save object module"""
import json


def save_to_json_file(my_obj, filename):
    """Save function"""
    with open(filename, mode="w", encoding="utf-8") as file:
        save_file = json.dump(my_obj, file)
        return save_file
