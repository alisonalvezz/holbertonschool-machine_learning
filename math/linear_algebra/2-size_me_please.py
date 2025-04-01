#!/usr/bin/env python3
"""
matrix shape
"""


def matrix_shape(matrix):
    """
    Calculates the shape of the matrix
    Attributes:
        matrix: the matrix to take the shape
    Return:
        list of integers
    """
    shape = []
    shape.append(len(matrix))
    if isinstance(matrix[0], list):
        shape.extend(matrix_shape(matrix[0]))
    return shape
