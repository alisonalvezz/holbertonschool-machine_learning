#!/usr/bin/env python3
"""
sum total
"""


def summation_i_squared(n):
    """
    calculates the sum of i^2 from 1 to n
    """
    if type(n) is not int or n < 1:
        return None
    return n * (n + 1) * (2 * n + 1) // 6
