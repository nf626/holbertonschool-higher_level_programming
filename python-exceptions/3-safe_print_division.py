#!/usr/bin/python3

def safe_print_division(a, b):
    #zeroDivisionError, typeerror
    divide = 0
    try:
        divide = a / b
    except (ZeroDivisionError, TypeError):
        None
    finally:
        print("Inside result: {}".format(divide))
    return (divide)
