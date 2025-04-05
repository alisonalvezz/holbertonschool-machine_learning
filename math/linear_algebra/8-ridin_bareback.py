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
    if not mat1 or not mat2 or len(mat1[0]) != len(mat2):
        return None

    new_mat = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            col_j = [mat2[k][j] for k in range(len(mat2))]
            dot_prod = 0    
            row_i = mat1[i]
            for k in range(len(mat1[0])):
                dot_prod += row_i[k] * col_j[k]
            row.append(dot_prod)
        new_mat.append(row)
    return new_mat
