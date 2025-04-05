#!/usr/bin/env python3
"""
gettin cozy
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    concatenates two matrices along a specific axis
    attributes:
        mat1: first matrix to concatenate
        mat2: second matrix
        axis: the axis along which to concatenate (0 for rows, 1 for columns)
    return:
        a new matrix concatenated or none if cannot concatenate
    """
    if (axis == 0 and any(len(row) != len(mat1[0]) for row in mat2)) or \
       (axis == 1 and len(mat1) != len(mat2)):
        return None
    result = []

    if axis == 0:
        for row in mat1:
            result.append(row[:])

        for row in mat2:
            result.append(row[:])

    elif axis == 1:
        for i in range(len(mat1)):
            new_row = mat1[i] + mat2[i]
            result.append(new_row)

    return result
