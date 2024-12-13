#!/usr/bin/env python3

"""
across the planes
"""


def add_matrices2D(mat1, mat2):
    """
    Adds two matrices element-wise
    Attributes:
        mat1: first matrix to add
        mat2: second matrix to add
    Returns:
        A new matrix, but None if they
        arent the same shape
    """
    if len(mat1) != len(mat2) or any(
        len(row1) != len(row2) for row1, row2 in zip(mat1, mat2)
    ):
        return None

    return [
        [a + b for a, b in zip(row1, row2)] for row1, row2 in zip(mat1, mat2)
    ]
