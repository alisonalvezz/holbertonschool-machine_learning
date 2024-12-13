#!/usr/bin/env python3

"""
ridin bareback
"""


def mat_mul(mat1, mat2):
    """
    Function that performs matrix multiplication
    Attributes:
        mat1: first matrix to multiplicate
        mat2: second matrix to multiplicate
    Returns:
        A new matrix, None if the two matrices cannot
        be multiplicated.
    """
    if len(mat1[0]) != len(mat2):
        return None
    
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]

    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result
