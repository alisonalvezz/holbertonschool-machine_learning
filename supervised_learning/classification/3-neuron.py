#!/usr/bin/env python3
"""
neuron
"""


import numpy as np


class Neuron:
    """Class that defines a single neuron performing binary classification"""

    def __init__(self, nx):
        """Initialize the neuron"""
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be positive")
        
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0
    
    @property
    def W(self):
        return self.__W
    
    @property
    def b(self):
        return self.__b
    
    @property
    def A(self):
        return self.__A
    
    def forward_prop(self, X):
        """Calculates the forward propagation of the neuron"""
        Z = np.matmul(self.__W, X) + self.__b 
        """multiplication between weight and the input matrix plus the bias"""
        self.__A = 1 / (1 + np.exp(-Z))
        """sigmoid/activation function"""
        return self.__A

    def cost(self, Y, A):
        """Calculates the cost using logistic regression loss function"""
        m = Y.shape[1]
        cost = -np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
        return cost
