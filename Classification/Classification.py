# Student Name:   Onur Onel
# Student No:     0865803
# Trent Email:    onuronel@trentu.ca
# Date:           08.03.2025
# Lab 8:          Classification

# This program applies two machine learning classification algorithms
# - Decision Tree 
# - k-Nearest Neighbors (k-NN) to classify the well-known Iris dataset.

# A Decision Tree is a downward-growing tree model used to make predictions by 
# recursively splitting the dataset based on the rules
# - It works well with both numerical and categorical data.
# - It creates decision rules that are easy to interpret.
# - It may suffer from overfitting, especially when the tree is too deep.

# k-NN is a distance-based classifier that assigns a class to a sample 
# based on the majority vote of its 'k' nearest neighbors.
# - It is simple and effective but can be computationally expensive.
# - It requires feature scaling because it relies on distance calculations.
# - The choice of 'k' affects accuracy 

# In supervised learning, we split data into:
# - Training Set: Used to train (learn) the model.
# - Testing Set: Used to evaluate how well the model generalizes to new data.

import sklearn
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

# Load the Iris dataset and extract features X and labels y
X, y = load_iris(return_X_y=True)

# Split dataset into training 67% and testing 33% sets
X_trainingData, X_testData, y_trainingData, y_testData = train_test_split(X, y, test_size=0.33)

# Decision Tree Classifier
DesicionTree = DecisionTreeClassifier()  # Initialize Decision Tree 
DesicionTree.fit(X_trainingData, y_trainingData)  # Train the classifier on training data
DtPrediciton = DesicionTree.predict(X_testData)  # Make predictions on test data

# Print classification report and confusion matrix 
print("Decision Tree Classification Report:")
print(classification_report(y_testData, DtPrediciton))  # Evaluate classification report
print("Decision Tree Confusion Matrix:")
print(confusion_matrix(y_testData, DtPrediciton))  # Display confusion matrix

# Scaling is essential for distance-based algorithms (k-NN)
Knn = KNeighborsClassifier(n_neighbors=5)  # Initialize k-NN classifier with k=5
scaler = StandardScaler()  # Initialize standard scaler

# Scale the training and testing data
X_trainingData_scaled = scaler.fit_transform(X_trainingData)  # Fit & transform training data
X_testData_scaled = scaler.transform(X_testData)  # Transform test data 

# Train k-NN classifier on scaled training data
Knn.fit(X_trainingData_scaled, y_trainingData)

# Make predictions using k-NN classifier on scaled test data
KnnPrediction = Knn.predict(X_testData_scaled)

# Print classification report and confusion matrix for k-NN
print("\nkNN Classification Report:")
print(classification_report(y_testData, KnnPrediction))  # Evaluate classification report
print("kNN Confusion Matrix:")
print(confusion_matrix(y_testData, KnnPrediction))  # Display confusion matrix


