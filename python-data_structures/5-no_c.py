#!/usr/bin/python3

def no_c(my_string):
    new_str = str()
    for i in my_string:
        if i != 'c' and i != 'C':
            new_str = new_str + i
    return new_str
