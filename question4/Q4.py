#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 15:02:15 2018
@author: Ssong

CTA200H 2018 Problem Set 1 
Question 4 
"""
import numpy as np
import matplotlib.pyplot as plt

z = 0
for x in np.arange(-2,2):
    for y in np.arange(-2,2):
        c = x + y*1j 
        z = z**2 + c
        print(z)
    
# creates array (c2d) of complex numbers x in the range of (-2,2) for the 
# real part, and in the range (-2j, 2j) for the complex part. 
arr11d = np.linspace(-2, 2, 1000)
arr21d = np.linspace(-2j, 2j, 1000)
arr12d, arr22d = np.meshgrid(arr11d, arr21d)
c2d = arr12d + arr22d

#takes array of complex numbers and maximum number of iterations, and 
#return an array of the number of iterations necessary for divergence at 
# each grid point. 
#optimized function 
def div(c,n):
    z = 0 
    for i in range(n):
        if abs(z) > 2:  
            return i 
        z = z**2 + c 
    return n 

new = np.vectorize(div)(c2d, n)

plt.imshow(new, extent = (-2, 2, -2, 2), cmap = "hot") 
plt.title("Imaginary vs. Real")
plt.xlabel("Real Component")
plt.ylabel("Imaginary Component")
plt.show()



