#!/usr/bin/env python3
"""
frequency
"""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """
    frequency
    """

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    plt.title('Project A')
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
    plt.xticks(np.arange(0, 110, 10))
    plt.axis([0, 100, 0, 30])
    plt.show()
