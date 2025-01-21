#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return new_list
"""
for x in a:
    if x == 30:
        b.append(99)
    else:
        b.append(x)
"""
