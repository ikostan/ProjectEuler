#!/usr/bin/python


import unittest
import os
from Problem_3.problem_3 import get_largest_factor


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_find_max_prime_factor(self):
        number = 13195
        prime_factors = [5, 7, 13, 29]
        max_factor = max(prime_factors)
        self.assertEqual(max_factor, get_largest_factor(number))

    def test_find_max_prime_factor_2(self):
        number = 600851475143 
        prime_factors = [71, 839, 1471, 6857]
        max_factor = max(prime_factors)
        self.assertEqual(max_factor, get_largest_factor(number))


if __name__ == '__main__':
    unittest.main()
