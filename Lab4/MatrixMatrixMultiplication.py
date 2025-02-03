# Student Name:   Onur Onel
# Student No:     0865803
# Trent Email:    onuronel@trentu.ca
# Date:           01.22.2025

# Lab 4: Matrix Multiplication Runtime Measurements

# Optimizing matrix multiplication is important for performance in AI, graphics, and scientific computing.
# The standard matrix multiplication algorithm, based on its mathematical definition, has a time complexity of O(n^3), but faster algorithms exist.
# For example, Strassen’s algorithm reduces the complexity to O(n^2.8), and even more advanced methods achieve further improvements.

# In order to correctly multiply two matrices, the following conditions must met:
# - The number of columns in the first matrix must be equal to the number of rows in the second matrix.
# - Since there is a shared property between the two matrices, we need three loop variables (i, j, k).

# source ~/venv/bin/activate
# python -m idle.lib idle

import random
import time
from memory_profiler import profile

# Multiplication of two matrices using the standard algorithm
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

size=int(input("Enter size: "))

r1=size
c1=size
r2=size
c2=size


A=[[0 for i in range(c1)] for j in range(r1)] #initialize matrix A

#input matrix A
for i in range(r1):
    for j in range(c1):
        x=random.randint(1,100)
        A[i][j]=x

B=[[0 for i in range(c2)] for j in range(r2)] #initialize matrix B

#input matrix B
for i in range(r2):
    for j in range(c2):
        x=random.randint(1,100)
        B[i][j]=x

P=[[0 for i in range(c2)] for j in range(r1)] #initialize product matrix
#INSERT CODE TO START TIMER
startTime = time.time()
print(multiply())
#INSERT CODE TO STOP TIMER
endTime = time.time()
#INSERT CODE TO COMPUTE ELAPSED TIME
elapsedTime = endTime-startTime
#INSERT CODE TO PRINT OVERALL TIME (IN s, NUMBER OF ELEMENTS IN THE RESULT MATRIX, AND TIME PER ELEMENT (IN ms)
print("Elapsed Time: ", elapsedTime)

