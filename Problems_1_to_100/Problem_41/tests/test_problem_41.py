#!/usr/bin/python


import unittest
import os
from Problems_1_to_100.Problem_41.problem_41 import find_largest_pandigital_prime, \
    has_pandigital_pattern


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_has_pandigital_pattern_true(self):
        self.assertTrue(has_pandigital_pattern(2143))

    def test_has_pandigital_pattern_false(self):
        self.assertFalse(has_pandigital_pattern(23143))

    def test_basic(self):

        number = 2150
        expected = 2143
        self.assertEqual(expected, find_largest_pandigital_prime(number))

    def test_find_largest_pandigital_prime(self):
        number = 999999999
        expected = 0
        self.assertEqual(expected, find_largest_pandigital_prime(number))


if __name__ == '__main__':
    unittest.main()
