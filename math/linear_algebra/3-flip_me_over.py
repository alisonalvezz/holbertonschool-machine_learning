#!/usr/bin/env python3
"""
flip me over
"""


def matrix_transpose(matrix):
    """
    returns the tranpose of a 2D matrix
    Attributes:
        matrix: the matrix to transpose to 2D
    Returns:
        a new matrix
    """

    transpuesta = list(map(list, zip(*matrix)))
    return transpuesta
