# Student Name:   Onur Onel
# Student No:     0865803
# Trent Email:    onuronel@trentu.ca
# Date:           28.03.2025
# Lab 10:         Numpy

# As the number of elements in the array increases, the overall time required for each sorting algorithm and the total sum of the array elements grows accordingly. 
# Meanwhile, the mean and standard deviation remain relatively unchanged indicates that statistics are less sensitive to larger sample sizes. 
# As expected, sorting runtimes scale with array size, with quicksort is the fastest which matches their known time complexities.

import numpy as np
import random
import time

# Seed using current time
random.seed(time.time())

# Generate 1000 random integers between 1 and 100
randomNumbers = []
for i in range(100000):
    num = random.randint(1, 100)
    randomNumbers.append(num)

# Convert to NumPy array
numpyArray = np.array(randomNumbers)

# Display array statistics
print("Dimensions of the array:", numpyArray.ndim)
print("Shape of the array:", numpyArray.shape)
print("Data type of the array:", numpyArray.dtype)
print("Minimum value in the array:", numpyArray.min())
print("Maximum value in the array:", numpyArray.max())
print("Sum of the array elements:", numpyArray.sum())
print("Mean of the array:", numpyArray.mean())
print("Standard deviation of the array:", numpyArray.std())

# Quicksort elapsed time
startQs = time.time()
quickSort = np.sort(numpyArray, kind='quicksort')
endQs = time.time()
elapsedQs = (endQs - startQs) * 1000  

# Mergesort elapsed time
startMs = time.time()
mergeSort = np.sort(numpyArray, kind='mergesort')
endMs = time.time()
elapsedMs = (endMs - startMs) * 1000 

# Heapsort elapsed time
startHs = time.time()
heapSort = np.sort(numpyArray, kind='heapsort')
endHs = time.time()
elapsedHs = (endHs - startHs) * 1000  

# Print results
print("\nNumber of elements in the array:", numpyArray.size)

print("\nQuicksort:")
print("Elapsed time (ms):", elapsedQs)
print("Time per element (ms):", elapsedQs / numpyArray.size)

print("\nMergesort:")
print("Elapsed time (ms):", elapsedMs)
print("Time per element (ms):", elapsedMs / numpyArray.size)

print("\nHeapsort:")
print("Elapsed time (ms):", elapsedHs)
print("Time per element (ms):", elapsedHs / numpyArray.size)


