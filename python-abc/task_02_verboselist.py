#!/usr/bin/env python3
"""VerboseList module"""


class VerboseList(list):
    """VerboseList class"""
    def append(self, item):
        """Append method"""
        super().__init__(str(item))
        print("Added [{}] to the list.".format(item))

    def extend(self, other):
        """Extend method"""
        print("Extended the list with {} items.".format(other))
    
    def remove(self, item):
        """Remove method"""
        super().remove(item)
        print("Removed [{}] from the list".format(item))

    def pop(self, item):
        """Pop method"""
        print("Popped [{}] from the list.".format(item))
