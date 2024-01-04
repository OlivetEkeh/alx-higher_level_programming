#!/usr/bin/python3
"""This is a function that devides all element of a matrix"""

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The input matrix.
        div (int or float): The divisor.

    Returns:
        list of lists: The modified matrix.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
                   if each row of the matrix doesn't have the same size,
                   or if div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    # Step 1: Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Step 2: Check if each row of the matrix has the same size
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Step 3: Check if div is a number (int or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Step 4: Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Step 5: Divide all elements of the matrix by div and round to 2 decimal places
    result_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    # Step 6: Return the modified matrix
    return result_matrix
