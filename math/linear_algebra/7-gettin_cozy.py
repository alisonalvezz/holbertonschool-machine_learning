#!/usr/bin/env python3

"""
gettin cozy
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis
    Attributes:
        mat1: the first matrix to concatenate
        mat2: the second matrix to concatenate
        axis: the axis to concatenate the matrices
    Return:
        A new matrix, but None if the two matrices cannot
        be concatenated
    """
    if axis == 0:
        if not all(len(row) == len(mat1[0]) for row in mat2):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]

    return None
