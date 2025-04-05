#!/usr/bin/env python3
"""
bracin the elements
"""


def np_elementwise(mat1, mat2):
    """
    performs element-wise addition, substraction and
    division
    attributes:
        mat1: first matrix to add, substract or divide
        mat2: second matrix to add, substract or divide
    return:
        a tuple containing the element-wise sum, difference,
        product, and quotient
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
