#!/usr/bin/env python3
"""
line up
"""


def add_arrays(arr1, arr2):
    """
    adds two arrays element-wise
    Attributes:
        arr1: first array to add
        arr2: second array to add
    Return:
        If the arrays arent the same shape, none
        else, a new list
    """
    result = []
    if len(arr1) == len(arr2):
        for i in range(len(arr1)):
            result.append(arr1[i] + arr2[i])
        return result
    return None
