#!/usr/bin/python3
"""Module: Divides a matrix"""


def matrix_divided(matrix, div):
    """ 
    
    Function that divides all elements of a matrix.
    
    Arguments:
        matrix - (list of lists) of integers/floats.
        div - integer or float
    
    Raise errors:
        TypeError - not int or float.
        TypeError - row not same size.
        TypeError - div not int or float.
        ZeroDivisionError - can't be zero.
    
    Return: new matrix with divided values.
            matrix should be divided by div,
            rounded to 2 decimal places.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(value, int) or isinstance(value, float))
                    for value in [coloumn for row in matrix for coloumn in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if isinstance(div, str):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
    return new_matrix
