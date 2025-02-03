#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList(list):
    """Sub-class of list"""
    def print_sorted(self):
        """Sorted list"""
        print(sorted(self))
