#!/usr/bin/bash python 
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 17:33:40 2018
@author: Ssong

CTA200H 2018 Problem Set 1 
Question 1 
Note: Have tried several methods of coding part c -- not sure where my
logic is failing. Currently getting "TypeError: argument of type 'NoneType' 
is not iterable" on line 32. 
"""
import os 
import glob

# user inputs 
find = input("Please input word to find: ")
replace = input("Please input word to replace: ")

# new directory "replace" created 
try:
    new_dir = os.makedirs(replace)
except OSError:
    pass 


files = glob.glob('./*.txt')
for i in files: 
    f1 = open(i, 'r')
    f2 = open(i, 'w') in new_dir  # part c. copy of files made in "replace" directory 
    for line in f1:
        f2.write(line.replace(find, replace)) # "find" replaced by "replace" 
    f1.close()
    f2.close()
 
