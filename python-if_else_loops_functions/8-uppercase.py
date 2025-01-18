#!/usr/bin/python3
"""To uppercase"""


def uppercase(str):
    '''prints a string in uppercase'''
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - (ord('a') - ord('A')))
        print("{:s}".format(c), end='')
    print("")
