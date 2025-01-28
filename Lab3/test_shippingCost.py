import unittest
import shippingCost

class TestShippingCost(unittest.TestCase):
    #first test case
    def test_shippingCostA(self):
        result = shippingCost.calculateCost(11)
        self.assertEqual(result, 4.75)
    #second test case
    def test_shippingCostB(self):
        result = shippingCost.calculateCost(7)
        self.assertEqual(result, 4.00)
    #third test case
    def test_shippingCostC(self):
        result = shippingCost.calculateCost(3)
        self.assertEqual(result, 3.00)
    #fourth test case
    def test_shippingCostD(self):
        result = shippingCost.calculateCost(1)
        self.assertEqual(result, 1.50)
    #edge case
    def test_shippingCostE(self):
        result = shippingCost.calculateCost(-3113)
        self.assertEqual(result, 1.50)
    #edge case
    def test_shippingCostF(self):
        result = shippingCost.calculateCost(0)
        self.assertEqual(result, 1.50)
