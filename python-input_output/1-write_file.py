#!/usr/bin/python3
"""Write file module"""


def write_file(filename="", text=""):
    """write function"""
    with open(filename, "w", encoding="utf-8") as f:
        write_data = f.write(text)
        return write_data
