# Student Name:   Onur Onel
# Student No:     0865803
# Trent Email:    onuronel@trentu.ca
# Date:           01.12.2025
# Source: https://docs.python.org/3/library/random.html
# Source: https://docs.python.org/3/library/time.html

# This module implements pseudo-random number generators for various distributions.
import random

# This module provides various time-related functions. 
import time

# Python's core random number generator algorithm is Mersenne Twister, which is extensively tested and reliable.
# Mersenne Twister is deterministic it is unsuitable for cryptographic applications or purposes requiring complete true randomness.

# Random integer: 0 <= x < 5
print(random.randrange(5)) # {0,1,2,3,4}

# Random integer: 2 <= x < 10 && x%2==0
print(random.randrange(2,10,2)) # {2,4,6,8}

# Random integer: 3 <= x < 9 && x%3==0
print(random.randrange(3,9,3)) # {3,6}

# Random float: 0.0 <= x < 1.0
print(random.random())

# Random float: 0.0 <= x < 1.0
print(random.uniform(0.0,1.0))

# Random binary: 1 || 0
print(random.getrandbits(1))

# Initialize the random number generator.
# If a is None, the current system time is used. If a is an int, it is used directly.
# With version 2, a str, bytes, or bytearray object gets converted to an int all are used.
random.seed(a=None, version=2) 
print(random.random()) # prints the result from the seed


# Same result with below.
random.seed(31)
print(random.random()) # prints the result from the seed

# Same result with above.
random.seed(31)
print(random.random()) # prints the result from the seed

# time.time() returns the seconds elapsed from Epoch, since January 1, 1970 
# *1000, Converts the seconds into milliseconds.
# round() Rounds to the nearest integer.
# Casts the final value to integer.
random.seed(int(round(time.time()*1000)))
print(random.random()) # prints the result from the seed