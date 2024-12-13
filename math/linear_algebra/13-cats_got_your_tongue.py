#!/usr/bin/env python3

"""
cats got your tongue
"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis
    Attributes:
        mat1: first matrix to concatenate
        mat2: second matrix to concatenate
    Return:
        a new numnpy.ndarray
    """
    return np.concatenate((mat1, mat2), axis=axis)
