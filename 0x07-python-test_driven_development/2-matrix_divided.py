#!/usr/bin/python3
def matrix_divided(matrix, div):
    """This divides all elements of a matrix
    Args:
        matrix: this is the matrix to divide
        div: this is the divisor
    Returns: This returns a new matrix
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("each element in each row of a matrix must be integer or float")
    if not matrix or not matrix[0]:
        raise ValueError("matrix must not be empty")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(element / div, 2) for element in row] for row in matrix]
    return result
