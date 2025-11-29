import unittest
from fractions import Fraction

from my_sum import sum
class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        data = [Fraction(1, 4), Fraction(1,4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()

#After the unittest function was called, the first test passed. This was the test of the sum of (1, 2, 3) against 6. But the testing for the sum of the list of fractions failed. 
#Because when you find the sum of all 3 fractions, the result comes out to 0.9. When the test_list_fraction function was tested, it failed because 0.9 does NOT equal 1. 