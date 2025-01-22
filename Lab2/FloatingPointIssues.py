# Student Name:   Onur Onel
# Student No:     0865803
# Trent Email:    onuronel@trentu.ca
# Date:           01.12.2025

# Lab 2: Floating Pint Issues
# https://docs.python.org/3/tutorial/floatingpoint.html
# import math
import decimal
from decimal import Decimal

# Floating-point numbers are stored as binary fractions in computer hardware. 
# Numbers that can be expressed as powers of 2 (1/2, 1/4,…) can be represented exactly.
# However, others can not be represented and they are instead approximated.


# ------
# print("Part1\n")

# print(".1 + .1 == .2 : ", .1+.1 == .2) # True 0.5
# print(".1 + .1 + .1 == .3 : ", .1+.1+.1 ==.3) # False 0.30
# print(".1 + .1 + .1 + .1 == .4 : ", .1+.1+.1 + .1 ==.4) # True 0.25

# ------
print("\nPart 2\n")

sum = 0
toAdd = .1
max = 10

for i in range (0, max, 1):
    sum = sum + toAdd
print("Iteration: ", max) 
print("Expected Sum:",max*toAdd) 
print("Actual Sum: ",sum) 
print("Error: ",(max*toAdd)-sum) 

# As the number of additions increases, small rounding errors in each operation grows,
# which is leading to larger error terms.The direction of the error varies depending on
# whether the rounding occurred upward or downward during the operation.

# error = 0
# value = 0
# iterations = 0
# addition = 0.1

# while error < addition: # This operations takes couple minutes 
#        value += toAdd
#        iterations += 1
#        error = -1*((iterations*toAdd)-value)
        
# print("Iterations needed to reach an error equal to 0.1:", iterations) # 264487878

# ------
# print("\nPart 3\n")

# As indicated above, numbers that can be expressed as powers of 2 (1/2, 1/4,…)
# are calculated perfectly, while other decimals approximated.
# Therefore;

# num = 0.5 # Or 0.25, 0.125, 0.0625 ...
# print("Number",num)
# if math.log2(num).is_integer():
#    print("Number ",num,"can be calculated perfectly")
# else:
#    print("Number ",num,"can be calculated using approximation")

# ------
print("\nPart 4\n")

total = Decimal(0)
increment = Decimal(0.1)
limit = 1000

for index in range(0, limit, 1):
    total += increment
print("Iteration: ", limit) 
print("Expected Sum:", Decimal(limit) * increment) 
print("Actual Sum: ", total)# Both the expected and actual sums match exactly
print("Error: ", (Decimal(limit) * increment) - total) # the error is 0 with 27 decimal places.


# Conclusion
# ----------

# When using floating-point numbers, errors are unavoidable due to the limitations of computer hardware.
# In contrast, the decimal module provides precise decimal arithmetic, avoiding binary rounding errors.
# With the decimal module, precise calculations remain consistent even as the iteration count increases.
# The only difference observed is that the error becomes extremely small (1E-26,2.8E-24) which is essentially zero.

    


