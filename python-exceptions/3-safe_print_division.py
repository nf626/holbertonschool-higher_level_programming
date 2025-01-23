#!/usr/bin/python3

def safe_print_division(a, b):
    #
    # zero division and type
    divide = 0
    try:
        divide = a / b
    except (ZeroDivisionError, TypeError):
        divide = None
    finally:
        print("Inside result: {}".format(divide))
    return (divide)
