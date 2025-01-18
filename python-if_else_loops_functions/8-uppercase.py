#!/usr/bin/python3
def uppercase(str):
    """makes all characters in a string uppercase."""
    for c in str:
        if (ord(c) >= 97 and ord(c) <= 122):
            c = chr(ord(c) - 32)
        print('{0}'.format(c), end="")
    print("")
