#!/usr/bin/python3
"""ASCII alphabet lowercase"""
for i in range(ord('a'), ord('z') + 1):
    print('{:c}'.format(i), end='')
