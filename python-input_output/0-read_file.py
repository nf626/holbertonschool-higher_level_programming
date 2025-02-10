#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """read file function"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
