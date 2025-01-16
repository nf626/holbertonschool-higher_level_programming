#!/usr/bin/python3
'''Hexadecimal printing'''
for i in range(0, 99):
    print(i, '=', "{0:#x}".format(i), end='\n')
