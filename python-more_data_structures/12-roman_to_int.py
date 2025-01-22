#!/usr/bin/python3

def roman_to_int(roman_string):

    if not isinstance(roman_string, str) or not roman_string:
        return 0

    numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }

    total = 0
    last = "I"
    for roman in roman_string[::-1]:
        if numerals[roman] < numerals[last]:
            total = total - int(numerals[roman])
        else:
            total = total + int(numerals[roman])
            last = roman
    return (total)
