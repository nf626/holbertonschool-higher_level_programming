#!/usr/bin/env python3
"""VerboseList module"""


class VerboseList(list):
    """VerboseList class"""
    def append(self, item):
        """Append method"""
        print("Added [item] to the list.")

    def extend(self, item, ):
        """Extend method"""
        print("Extended the list with [x] items.")
    
    def remove(self):
        """Remove method"""
        print("Removed [item] from the list")

    def pop(self):
        """Pop method"""
        print("Popped [item] from the list.")
