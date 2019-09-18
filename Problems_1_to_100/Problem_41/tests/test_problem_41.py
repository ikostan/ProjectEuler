#!/usr/bin/python

import unittest
import os
from Problems_1_to_100.Problem_41.problem_41 \
    import find_largest_pandigital_prime


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_find_largest_pandigital_prime(self):
        numbers = [7, 6, 5, 4, 3, 2, 1]
        expected = 7652413
        self.assertEqual(expected, find_largest_pandigital_prime(numbers))
