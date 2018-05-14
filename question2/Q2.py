#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 17:39:58 2018
@author: Ssong

CTA200H 2018 Problem Set 1 
Question 2 
"""

import math as m
import matplotlib.pyplot as plt 

# part a 
def binomial(n, k):
    if type(n) == int and type(k) == int: 
        if n >= 0 and k >= 0:
            if n >= k:
                return m.factorial(n) / ( ( m.factorial(k) ) * (m.factorial(n-k))) 
            elif k == 0:
                return 1 
        else: 
            print("Undefined") 
    else:
        print("Please enter an integer") 



# part b 
for n in range(21):
    for k in range(21):
        if n >= k:
            print(binomial(n,k))
        else: 
            break 
        
# part c 
def prob(n, k, p):
    return binomial(n,k)*p**k*(1-p)**(n-k)

# example application 
print(prob(4, 1, 0.250))

# part d 
for i in (10, 100, 1000):
    print(prob(i, 1, 0.250))
    
    plt.plot(i, prob(i, 1, 0.250), "r.")
    plt.xlabel("N times")
    plt.ylabel("Success")
    plt.title("Probability of hitting at least once vs. N")

