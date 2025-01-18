#!/usr/bin/python3
"""To uppercase"""


def uppercase(str):
    '''prints a string in uppercase'''
    for c in str:
        if ord(c) < 123 and ord(c) > 96:
            c = chr(ord(c) - 32)
        print("{}".format(c), end='')
    print()
