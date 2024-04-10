#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.
    Args:
        matrix: list of lists containing integers or floats
        div: divisor (int or float)
    Returns:
        new_matrix: new matrix with all elements divided by div
    Raises:
        TypeError: if matrix contains non-integer/float elements or if div is not an int/float
        ZeroDivisionError: if div is zero
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must contain only integers or floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("each row of the matrix must have the same size")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matrix
