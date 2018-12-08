# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 19:26:25 2018

Problem 2 on final exam review

@author: Patricia
"""
import numpy as np

# make a numpy array named x
x = []
for i in range(21):
    x.append(i)

print(x)
countUnder=0 # counts should be initialized to 0
countOver=0
for i in range(len(a)+1):
    if x[i] < 10:
        countUnder=countUnder+1
    elif x[i] > 10:
        countOver=countOver+1

print("There are this many values below 10 in x:",countUnder)
print("There are this many values above 10 in x:",countOver)

'''
original code
count=1
for i in range(1,10):
if x[count]>=10):
count=count+1
else:
count2=count2+1
print("There are this many values below 10 in x:",count))
print("There are this many values above 10 in x:",count2))
'''