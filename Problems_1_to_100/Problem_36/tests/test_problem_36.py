#!/usr/bin/python


import unittest
import os
from Problems_1_to_100.Problem_36.problem_36 import calc_sum_of_palindromic_numbers


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_calc_sum_of_palindromic_numbers(self):
        limit = 1000000
        expected = 872187
        self.assertEqual(expected, calc_sum_of_palindromic_numbers(limit))


if __name__ == '__main__':
    unittest.main()
