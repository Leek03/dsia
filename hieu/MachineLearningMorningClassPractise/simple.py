#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:21:48 2019

@author: hieu
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def abline(x,Y):
    """Plot a line from slope and intercept"""
    
    y_vals = predictPrice(x,Y)
#    plt.xlim(0, 10)
#    plt.ylim(-10, 60)
    plt.xlabel('No. of Rooms in the house')
    plt.ylabel('Price of house')
    plt.gca().set_aspect(0.1, adjustable='datalim')
    plt.plot(x,Y,'.',x, y_vals, '-')
    plt.show()

X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
# y = 1 * x_0 + 2 * x_1 + 3
y = np.dot(X, np.array([1, 2])) + 3
reg = LinearRegression().fit(X, y) #call the function 
print(reg.score(X, y))

print(reg.coef_)
print(reg.intercept_) 
print(reg.predict(np.array([[3, 5]])))

abline(X,y)

#fit predict and score. 