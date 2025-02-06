#!/usr/bin/env python3
"""Iter module"""


class CountedIterator:
    """Counter iterator class"""
    def __init__(self, iter, count):
        self.iterator = iter(some_iterable)
        self.count = count

    def get_count(self):
        """counts number of iteration"""
        self.count = 0
        return self.count

    def __next__(self):
        """next method to increment counter"""
        for item in self.iterator:
            self.count +=1
        return self.get_count()
