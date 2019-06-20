#!/usr/bin/python


import unittest
import os
from Problem_20.problem_20 import calc_factorial
from Problem_20.problem_20 import calc_sum_of_digits


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_calc_factorial(self):
        n = 10
        expected = 3628800
        self.assertEqual(expected, calc_factorial(n))

    def test_calc_sum_of_digits(self):
        expected = 3 + 6 + 2 + 8 + 8 + 0 + 0
        n = 10
        self.assertEqual(expected, calc_sum_of_digits(n))

    def test_100(self):
        expected = 648
        n = 100
        self.assertEqual(expected, calc_sum_of_digits(n))


if __name__ == '__main__':
    unittest.main()
