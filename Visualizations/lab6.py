# Student Name:   Onur Onel
# Student No:     0865803
# Trent Email:    onuronel@trentu.ca
# Date:           26.03.2025
# Lab 7:          Visualizations 

# Part 1
import numpy as np  
import matplotlib.pyplot as plt  
from pydataset import data  

iris = data('iris')  
firstTwo = tuple(iris.columns[:2])

plt.scatter(iris[firstTwo[0]], iris[firstTwo[1]])
plt.title('Scatter Plot')
plt.xlabel(firstTwo[0])  
plt.ylabel(firstTwo[1])  
plt.show()  

# Part 2
labels = 'virginica', 'setosa', 'versicolor'
sizes = [50, 50, 50]
plt.title('Pie Chart')
plt.pie(sizes, labels=labels)
plt.show()  

# Part 3
plt.hist(iris[firstTwo[0]])
plt.title('Histogram')
plt.xlabel(firstTwo[0])
plt.ylabel('Count')     
plt.show()  

# Part 4
fig, axes = plt.subplots(2, 2)
title = 'Onur Onel 0865803'

# Pie Chart 
labels = ['virginica', 'setosa', 'versicolor']
sizes = [50, 50, 50]
axes[0, 0].pie(sizes, labels=labels)
axes[0, 0].set_title(title)  

# Scatter Plot 
axes[0, 1].scatter(iris['Sepal.Length'], iris['Sepal.Width'], color='blue')
axes[0, 1].set_title(title)  
axes[0, 1].set_xlabel('Sepal.Length')  
axes[0, 1].set_ylabel('Sepal.Width')  

# Scatter Plot 
axes[1, 0].scatter(iris['Petal.Length'], iris['Petal.Width'], color='green')
axes[1, 0].set_title(title) 
axes[1, 0].set_xlabel('Petal.Length')  
axes[1, 0].set_ylabel('Petal.Width')

# Histogram 
axes[1, 1].hist(iris[firstTwo[0]])
axes[1, 1].set_title(title)  
axes[1, 1].set_xlabel(firstTwo[0])  
axes[1, 1].set_ylabel('Count')

plt.show()


