# Student Name:   Onur Onel
# Student No:     0865803
# Trent Email:    onuronel@trentu.ca
# Date:           01.12.2025

# Lab 2: Floating Pint Issues
# https://docs.python.org/3/tutorial/floatingpoint.html

# Floating-point numbers are stored as binary fractions in hardware. 
# Numbers that can be expressed as powers of 2 (1/2, 1/4,…) can be represented exactly.
# However, others can not be represented and they are instead approximated.


# ------
# print("Part1\n")

# print(".1 + .1 == .2 : ", .1+.1 == .2)
# print(".1 + .1 + .1 == .3 : ", .1+.1+.1 ==.3)
# print(".1 + .1 + .1 + .1 == .4 : ", .1+.1+.1 + .1 ==.4)

# ------
# print("\nPart2\n")

# sum = 0
# toAdd = .1
# max = 10

# for i in range (0, max, 1):
#        sum = sum + toAdd
# print("Iteration: ", max)
# print("Expected Sum:",max/10)
# print("Actual Sum: ",sum)
# print("Error: ",(max*toAdd)-sum)

# As the number of additions increases, small rounding errors in each operation accumulate,
# leading to larger error terms.The direction of the error varies depending on
# whether the rounding occurred upward or downward during the current operation.

# error = 0
# value = 0
# iterations = 0
# addition = 0.1

# while error < addition: # This operations takes couple minutes 
#        value += toAdd
#        iterations += 1
#        error = -1*((iterations*toAdd)-value)
        
# print("Iterations needed to reach an error equal to 0.1:", iterations) # Count: 264487878

# ------
# print("\nPart 3\n")
        


