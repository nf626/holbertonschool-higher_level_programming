#!/usr/bin/python3
"""Append file module"""


def append_write(filename="", text=""):
    """Append function"""
    with open(filename, "a", encoding="utf-8") as f:
        append_data = f.write(text)
        return append_data
