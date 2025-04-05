#!/usr/bin/env python3
"""
ridin bareback
"""


def mat_mul(mat1, mat2):
    """
    performs matrix multiplication
    attributes:
        mat1: first matrix to multiplicate
        mat2: second matrix
    return:
        a new matrix, none if cant be multiplied
    """

    if len(mat1[0]) != len(mat2):
        return None

    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            product = sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2)))
            row.append(product)
        result.append(row)
    return result
