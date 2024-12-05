#!/usr/bin/env python3
"""
flip me over
"""


def matrix_transpose(matrix):
    """
    Transposes matrices
    Attributes:
        matrix: the matrix to flip over
    """
    return [list(row) for row in zip(*matrix)]
