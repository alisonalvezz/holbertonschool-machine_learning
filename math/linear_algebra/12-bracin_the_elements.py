#!/usr/bin/env python3

"""
bracin the elements
"""


def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, substraction,
    multiplication and division
    Attributes:
        mat1: first matrix to perform
        mat2: second matrix to perform
    Returns:
        a tuple which contains element wise sum,
        difference, product and quotient
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
