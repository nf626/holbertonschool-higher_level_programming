#!/usr/bin/python3
"""Module: Text indentation"""

def text_indentation(text):
    """

    function that prints a text with 2 new lines after
    each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count = 0
    while (count < len(text) and text[count] == " "):
        count = count + 1

    