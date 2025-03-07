# Student Name:   Onur Onel
# Student No:     0865803
# Trent Email:    onuronel@trentu.ca
# Date:           01.12.2025

# Estimating Pi using the Monte Carlo Method
# ------------------------------------------
# As we increase the number of iterations, our estimate of pi becomes more and more accurate.
# When I raise the iteration count to a billion, my CPU takes a couple of minutes to finish.
# Theoretically, finding the exact value of pi would require infinite iterations that takes infinitely long run time.
import random
import math
import time

inside = 0 # counter
outside = 0 # counter
iterations = 10000000

random.seed(int(round(time.time()*1000))) # Ensuring different seed
for i in range(iterations):
    # select two random numbers between 0 and 1
    x = random.random() # Random x in [0,1]
    y = random.random() # Random y in [0,1]
    
    # calculate distance from origin
    distance = math.sqrt((x*x) + (y*y)) # Distance from origin
    
    # increment the appropriate counter
    if distance <= 1: # Inside quarter circle
        inside += 1
    else: 
        outside += 1
    

# calculate the value of Pi 
MonteCarlo_PI = 4 * (inside/iterations) 

# print result
print("Count of the points inside the circle: ",inside)
print("Count of the points outside the circle: ",outside)
print("Pi actually equals to: ", math.pi)
print("Our Pi estimation with Monte Carlo method: ",MonteCarlo_PI)



