from fractions import Fraction
import unittest
from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
      # Test that it can sum a list of integers
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
      # Test that it can sum a list of fractions
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
    #The code is failing because the sum function is not defined in the my_sum module. 
    # The sum function needs to be implemented in the my_sum/__init__.py file for the tests to pass.