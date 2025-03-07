# Student Name:   Onur Onel
# Student No:     0865803
# Trent Email:    onuronel@trentu.ca
# Date:           07.03.2025
# Lab 8:          Clustering

# This program demonstrates the use of K-Means clustering on the Iris dataset using scikit-learn.
# K-Means is an unsupervised machine learning algorithm that partitions data into k clusters.
# The Iris dataset consists of 150 samples, each with four numerical features: 
#   - Sepal Length
#   - Sepal Width
#   - Petal Length
#   - Petal Width
# We apply K-Means clustering to find groupings in the data.
# The Elbow Method is used to determine the optimal number of clusters.

import sklearn
import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.datasets import load_iris
from sklearn import preprocessing
from sklearn.cluster import KMeans

# Load Iris dataset
data = load_iris()
numData = data['data']
scaledData = preprocessing.scale(numData) # Scaling is essential for distance-based algorithms


# Calculate sum of squared errors
SSE = []
for i in range(1, 9): # Iterating cluster sizes 
    kmeans = KMeans(n_clusters=i, max_iter=300) # Initialize KMeans with i clusters
    kmeans.fit(scaledData) # Fit the model to the scaled data
    SSE.append(kmeans.inertia_) # Store the SSE for each k value

# Plot SSE against the number of clusters 
plt.plot(range(1, 9), SSE) 
plt.suptitle('Onur Onel 0865803 March 7 2025', fontsize=12, fontweight='bold')
plt.title('Finding Number of Clusters (k)') # Subtitle
plt.xlabel('Number of Clusters') # X-axis label
plt.ylabel('Sum of Squared Errors') # Y-axis label
plt.show() # Display the plot to identify the k value (Elbow Method)

# Create subplots 
fig, axes = plt.subplots(1, 2,)  
fig.suptitle('Onur Onel  0865803 March 7 2025', fontsize=12, fontweight='bold')

# Fit KMeans with clusters and predict cluster labels
kmeans = KMeans(n_clusters=2, max_iter=300) # Initialize KMeans with 2 clusters
kmeans.fit(scaledData) # Fit the model
predictions = kmeans.predict(scaledData) # Predict cluster labels for each sample

# Plotting clusters using first two features from the scaled data (k=2)
axes[0].scatter(scaledData[:, 0], scaledData[:, 1], c=predictions)
axes[0].set_title('Onur Onel - KMeans Clustering (k=2)') # Title for k=2 plot
axes[0].set_xlabel('Sepal Length') # X-axis label
axes[0].set_ylabel('Sepal Width') # Y-axis label

# Fit KMeans with clusters and predict cluster labels
kmeans = KMeans(n_clusters=3, max_iter=300) # Initialize KMeans with 3 clusters
kmeans.fit(scaledData) # Fit the model
predictions = kmeans.predict(scaledData) # Predict cluster labels for each sample

# Plotting clusters from the scaled data (k=3)
axes[1].scatter(scaledData[:, 0], scaledData[:, 1], c=predictions)
axes[1].set_title('Onur Onel - KMeans Clustering (k=3)') # Title for k=3 plot
axes[1].set_xlabel('Sepal Length') # X-axis label
axes[1].set_ylabel('Sepal Width') # Y-axis label

plt.show() # Display the clustering results