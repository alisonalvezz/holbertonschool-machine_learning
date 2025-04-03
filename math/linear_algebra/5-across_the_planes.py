#!/usr/bin/env python3
"""
across the planes
"""


def add_matrices2D(mat1, mat2):
    """
    adds two matrices element-wise.
    Attributes:
        mat1: First matrix.
        mat2: Second matrix.
    Returns:
        None if they aren't the same shape, otherwise a new matrix with the addition.
    """
    if len(mat1) != len(mat2) or any(
            len(row1) != len(row2) for row1, row2 in zip(mat1, mat2)):
        return None

    result = []
    for i in range(len(mat1)):
        fila = [mat1[i][j] + mat2[i][j] for j in range(len(mat1[i]))]
        result.append(fila)

    return result
