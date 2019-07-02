#!/usr/bin/python


import unittest
import os
from Problems_1_to_100.Problem_41.problem_41 import find_largest_pandigital_prime


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_find_largest_pandigital_prime(self):
        number = 9876543210
        expected = 0
        self.assertEqual(expected, find_largest_pandigital_prime(number))


if __name__ == '__main__':
    unittest.main()
