#!/usr/bin/python3
"""ASCII reverse lowercase, uppercase alt alphabet"""
for char in range(ord('Z'), ord('A') - 1, -1):
    if char % 2:
        print("{:c}".format(char), end="")
    else:
        print('{:c}'.format(char + 32), end="")
