#!/usr/bin/python3
"""To uppercase"""


def uppercase(str):
    '''prints a string in uppercase'''
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            c = chr(ord(c) - 32)
        print("{0}".format(c), end="")
    print("")
