# Student Name:   Onur Onel
# Student No:     0865803
# Trent Email:    onuronel@trentu.ca
# Date:           01.28.2025
# Lab 3: Debugging and Testing

# This Lab demonstrates the implementation of debugging techniques 
# and creating test cases using the unittest framework.

# Importing the unittest module 
import unittest

# Importing the shippingCost 
import shippingCost

# Defining a test class
class TestShippingCost(unittest.TestCase):
    
    # First test case: Test calculateCost with input 11
    # Expected output: 4.75
    def test_shippingCostA(self):
        result = shippingCost.calculateCost(11)
        self.assertEqual(result, 4.75)

    # Second test case: Test calculateCost with input 7
    # Expected output: 4.00
    def test_shippingCostB(self):
        result = shippingCost.calculateCost(7)
        self.assertEqual(result, 4.00)

    # Third test case: Test calculateCost with input 3
    # Expected output: 3.00
    def test_shippingCostC(self):
        result = shippingCost.calculateCost(3)
        self.assertEqual(result, 3.00)

    # Fourth test case: Test calculateCost with input 1
    # Expected output: 1.50
    def test_shippingCostD(self):
        result = shippingCost.calculateCost(1)
        self.assertEqual(result, 1.50)

    # Edge case one: Test calculateCost with negative input (-3113)
    # Expected output: 1.50 
    def test_shippingCostE(self):
        result = shippingCost.calculateCost(-3113)
        self.assertEqual(result, 1.50)

    # Edge case two: Test calculateCost with input 0
    # Expected output: 1.50 
    def test_shippingCostF(self):
        result = shippingCost.calculateCost(0)
        self.assertEqual(result, 1.50)

