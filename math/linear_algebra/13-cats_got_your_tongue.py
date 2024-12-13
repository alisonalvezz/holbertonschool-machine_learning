#!/usr/bin/env python3

"""
cats got your tongue
"""


def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis
    Attributes:
        mat1: first matrix to concatenate
        mat2: second matrix to concatenate
    Return:
        a new numnpy.ndarray
    """
    import numpy as np
    return np.concatenate((mat1, mat2), axis=axis)