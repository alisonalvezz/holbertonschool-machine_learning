#!/usr/bin/env python3
"""
line
"""

import numpy as np
import matplotlib.pyplot as plt

def line():
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))

    plt.xlim(0, 10)
    plt.plot(range(11), y, color='r')
    plt.show()

line()