#!/usr/bin/env python3
"""Iter module"""


class CountedIterator:
    """Counter iterator class"""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """next method to increment counter"""
        self.count = self.count + 1
        return next(self.iterator)

    def get_count(self):
        """counts number of iteration"""
        return self.count
