#!/usr/bin/python3
"""Pascal triangle module"""


def pascal_triangle(n):
    """pascal triangle function"""
    if n <= 0:
        return []

    pascal = [[1]]

    for coloumn in range(1, n):
        row_pos = [1]
        for row in range(1, coloumn):
            row_pos.append(pascal[coloumn-1][row-1] + pascal[coloumn-1][row])
        row_pos.append(1)
        pascal.append(row_pos)
    return pascal
