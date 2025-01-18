#!/usr/bin/python3
def print_last_digit(number):
    '''print last digit of number'''
    last_digit = abs(number) % 10
    if number < 0:
        print("{:d}".format(last_digit), end='')
        return last_digit
    else:
        print("{:d}".format(last_digit), end='')
        return last_digit
