#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end='')
            num = num + 1
        except Exception:
            None
    print()
    return (num)
