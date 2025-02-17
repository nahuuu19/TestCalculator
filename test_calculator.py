import unittest
import math
from calculator import Calculator

class TestCalculator(unittest.TestCase):


    def setUp(self):
        self.calculator = Calculator()

    def test_sum(self):
        self.assertEqual(self.calculator.sum(3,4),7)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2,2),4)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5,4),1)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10,2), 5)
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(10,0)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(16),4.0)

    def test_calculate_pi(self):
        self.assertAlmostEqual(self.calculator.calculate_pi(), math.pi)

if __name__ == "__main__":
    unittest.main()
