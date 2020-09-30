# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 14:39:41 2018

@author: drodr
"""
a#YellowIguana
#10/30/18
#Challenge 4

#https://stackoverflow.com/questions/20130227/matplotlib-connect-scatterplot-points-with-line-python
#line 79
#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.viridis.html
#line 83
#https://stackoverflow.com/questions/43482446/python-scatter-plot-different-colors-depending-on-value
#line 82
#https://www.programiz.com/python-programming/methods/list/sort
#line 71

import numpy as np
import math
import matplotlib.pyplot as mplot

userinput = input("Enter a k-value: ")

us_outline = open("data_ch4/us_outline.csv", "r")
outline = us_outline.read()
outline = outline.replace(", ", ",")
outline = outline.split("\n")

xaxis = []
yaxis = []

for index in range(0, len(outline)):
    outline[index] = outline[index].split(",")
    xaxis.append(float(outline[index][0]))
    yaxis.append(float(outline[index][1]))

reference = open("data_ch4/data.csv", "r")
data = reference.read()
data = data.split("\n")

reference_xaxis = []
reference_yaxis = []
reference_change = []

for index in range(0, len(data)):
    data[index] = data[index].split(",")
    reference_xaxis.append(float(data[index][0]))
    reference_yaxis.append(float(data[index][1]))
    reference_change.append(float(data[index][2]))

def dist(a, b):
    return math.sqrt(math.pow(a[0]-b[0],2)+math.pow(a[1]-b[1],2))

reconstructed_xaxis = []
reconstructed_yaxis = []
reconstructed_change = []

for i in range (195):
    for j in range(121):
        reconstructed_yaxis.append(j)
        reconstructed_xaxis.append(i)
        distance = []
        for k in range(len(data)):
            dist_xy = dist([i,j], [reference_xaxis[k], reference_yaxis[k]])
            distance.append([dist_xy, k])
        distance.sort(key = lambda x : x[0])
        distance_list = distance[:int(userinput)]
        average = 0
        for l in range(len(distance_list)):
            lowest_k = distance_list[l][1]
            average += reference_change[lowest_k]
        average /= int(userinput)
        reconstructed_change.append(average)
#print(reconstructed_yaxis)

#mplot.scatter(reference_xaxis, reference_yaxis, c = reference_change)
mplot.scatter(reconstructed_xaxis, reconstructed_yaxis, c = reconstructed_change)
mplot.viridis()
#mplot.scatter(xaxis, yaxis, c = "Black")
mplot.plot(xaxis, yaxis, c = "Black")
mplot.show()
