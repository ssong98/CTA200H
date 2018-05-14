#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 15:07:51 2018
@author: Ssong

CTA200H 2018 Problem Set 1 
Question 5 
 
"""
import numpy as np 
import sympy as sp
import matplotlib.pyplot as plt

# numeric derivative
x = sp.symbols("x")
a = sp.diff((x**2 - x), x)
print(a)

# definition of derivative
X = np.logspace(np.log10(10**-14), np.log10(10**-4))
XX = X.reshape(1,50)

def der(f):
    def df(x):
        return (f(x + delta) - f(x))/delta 
    return df
    

def g(x): 
    return x**2 - x 

dg = der(g)

# approximate derivative for a log-spaced range of values of delta 
for delta in X:
    dg = der(g)
    num = dg(1)
    print(num)
    plt.plot(XX, np.array(num), "r.")
    plt.xlabel("Delta Value Range")
    plt.ylabel("Approximate Derivative at x = 1")
    plt.title("Approximate Derivative Corresponding to Different Delta Values")

