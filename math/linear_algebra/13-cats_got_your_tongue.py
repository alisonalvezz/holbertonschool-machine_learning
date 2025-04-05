#!/usr/bin/env python3
"""
cats got your tongue
"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    concatenates two matrices along a specific axis
    attributes:
        mat1: first matrix to concatenate
        mat1: second matrix to concatenate
        axis: axis to concatenate along
    return:
        a new numpy.ndarray
    """
    return np.concatenate((mat1, mat2), axis=axis)
