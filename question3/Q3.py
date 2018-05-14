#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 17:55:09 2018
@author: Ssong

CTA200H 2018 Problem Set 1 
Question 3 
Note: Not sure where I'm going wrong for both approaches.
Specifically, I am having trouble with integrating with 
respect to theta while treating variable x as essentially
constant.  
"""
from sympy import integrate, cos, sin 
from sympy.abc import x, theta
import scipy as sp 
import numpy as np 

# approach 1 
def Bessel(theta, x):
    for m in range(10):
        return np.cos(m*theta - x*np.sin(theta))

I = sp.integrate.nquad(Bessel, [[(0, np.pi)], [x]])

print(I)

# approach 2 
for m in range(5):
    f = cos(m*theta - x*sin(theta))
    I = integrate(f, (theta, 0, np.pi))
    print(I)
    
