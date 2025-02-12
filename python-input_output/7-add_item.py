#!/usr/bin/python3
"""Load, Add, Save module"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
my_list = sys.argv
save_to_json_file(my_list, filename)
