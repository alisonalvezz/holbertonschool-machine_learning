#!/usr/bin/env python3

"""
line up
"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise
    Attributes:
        arr1: first array to add
        arr2: second array to add
    Return:
        A new list but if the arrays arent the
        same shape, it returns None.
    """
    if len(arr1) != len(arr2):
        return None

    return [a + b for a, b in zip(arr1, arr2)]
