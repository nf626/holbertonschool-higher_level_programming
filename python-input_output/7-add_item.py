#!/usr/bin/python3
"""Load, Add, Save module"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
add_item = "add_item.json"

try:
    # Loads file
    new_obj = load_from_json_file(add_item)
except FileNotFoundError:
    # Check if file found, does not exist create empty list
    new_obj = []

new_obj.extend(sys.argv[1:])
save_to_json_file(new_obj, add_item)
