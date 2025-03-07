# Student Name:   Onur Onel
# Student No:     0865803
# Trent Email:    onuronel@trentu.ca
# Date:           02.03.2025
# Lab 4: Matrix Multiplication & Runtime Measurements


# Question 1:
# Matrix multiplication is essential for performance in graphics, scientific computing and more.
# The standard matrix multiplication algorithm, based on classic mathematical definition,
# has a time complexity of O(n^3), but faster algorithms exist (i.e. Strassen’s Algorithm).
# The standard algorithm's runtime grows quickly as the matrix size increases.  
# This happens because there are 3 loops, each going through n elements,  
# making the total number of operations (n x n x n) n^3.

# Question 2:
# The CPU handles matrix operations and processes them sequentially (modern ones uses multi-threading).  
# As we increase the matrix size, the number of operations grows cubically leading to longer runtimes.
# Other than Algorithmic improvements, we can accelerate performance by parallelizing the operation with GPUs or using optimization libraries.

import random
import time
from memory_profiler import profile # Module for Monitoring Memory Consumption

# In order to correctly multiply two matrices, the following conditions must met:
# - The number of columns in the first matrix must be equal to the number of rows in the second matrix.
# - Since there is a shared property between the two matrices, we need three loop variables (i, j, k).

# The profile module measures memory usage and performance during matrix multiplication.
# It helps track how much memory is being used while executing the function multiply().
# Multiplication of two matrices
@profile
def multiply():
    # Iterate over each row of matrix P
    for i in range(size):
        # Iterate over each column of matrix P
        for j in range(size): 
            # Iterate over the shared dimension of matrices A and B
            for k in range(size):
                P[i][j] += (A[i][k] * B[k][j]) # P(IxJ) = A(IxK) * B(KxJ)
    return P # Return the result matrix P

# Since matrices defined as square matrices (n x n) down below simply; 
size=int(input("Enter size: ")) # Get size of the new matrix

r1=size # M1 row = given size
c1=size # M1 col = given size
r2=size # M2 row = given size
c2=size # M2 col = given size


A=[[0 for i in range(c1)] for j in range(r1)] #initialize matrix A

#input matrix A
for i in range(r1): # Iterate through rows
    for j in range(c1): # Iterate through cols
        x=random.randint(1,100) # Get random (1 <= x <= 100)
        A[i][j]=x # Fill the cells

B=[[0 for i in range(c2)] for j in range(r2)] #initialize matrix B

#input matrix B
for i in range(r2): # Iterate through rows
    for j in range(c2): # Iterate through cols
        x=random.randint(1,100) # Get random (1 <= x <= 100)
        B[i][j]=x # Fill the cells

P=[[0 for i in range(c2)] for j in range(r1)] #initialize product matrix

# Measures runtime using time.time(), which records the start and end time.
# It calculates how much time is spent  on each element by dividing the total time by the number of elements.
# Start timer
startTime = time.time()

# Multiply matrices
multiply()

# Stop timer
endTime = time.time()

# Compute elapsed time in milliseconds
elapsedTime = (endTime - startTime) * 1000

# Compute time per element in milliseconds
timePerElement = (elapsedTime / (size * size)) 

# Print results
print("Number of elements of result matrix: ", size * size)
print("Elapsed time in ms: ", elapsedTime)
print("Time spend per element in ms: ", timePerElement)


