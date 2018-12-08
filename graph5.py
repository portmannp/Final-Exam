# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 22:51:40 2018

Problem 5 on the final exam review
Write the Python code required to plot the values contained in a vector y vs 
the values in a vectory x and add a spline best fit line to the scatter plot.

@author: Patricia
"""

import numpy as np #for numpy array
import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6,7,8,9,10]
y = [0,2,4,6,8,10,12,14,16,18,20]

graph = plt.scatter(x, y)
graph = plt.title('Problem 5 Review Final')
plt.xlabel('x') # x axis label
plt.ylabel('y') # y axis label
z = np.polyfit(x,y,1) # finds the linear line of best fit
p = np.poly1d(z)
plt.plot(x,p(x),"r--")
plt.show()
