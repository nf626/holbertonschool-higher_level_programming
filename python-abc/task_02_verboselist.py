#!/usr/bin/env python3
"""VerboseList module"""


class VerboseList(list):
    """VerboseList class"""
    def append(self, item):
        """Append method"""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iter):
        """Extend method"""
        super().extend(iter)
        print("Extended the list with {} items.".format(len(iter)))
    
    def remove(self, item):
        """Remove method"""
        super().remove(item)
        print("Removed [{}] from the list".format(item))

    def pop(self, item):
        """Pop method"""
        super().pop(item)
        print("Popped from the list.")
