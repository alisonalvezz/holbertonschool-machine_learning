#!/usr/bin/env python3
"""
frequency
"""


import numpy as np
import matplotlib.pyplot as plt

def frequency():

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    plt.ylabel('Number of Students')
    plt.xlabel('Grades')
    plt.title('Project A')
    plt.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
    plt.xticks(range(0, 101, 10))
    plt.yticks(range(0, 35, 5))
    plt.show()

frequency()
