#!/usr/bin/python


import unittest
import os
from Problems_1_to_100.Problem_6.problem_6 import sum_squares_of_numbers
from Problems_1_to_100.Problem_6.problem_6 import square_of_sums
from Problems_1_to_100.Problem_6.problem_6 import square_diff


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_sum_of_squares(self):
        expected = 385
        start = 1
        end = 10
        self.assertEqual(expected, sum_squares_of_numbers(start, end))

    def test_square_of_sums(self):
        expected = 3025
        start = 1
        end = 10
        self.assertEqual(expected, square_of_sums(start, end))

    def test_basic(self):
        start = 1
        end = 10
        expected = 2640
        self.assertEqual(expected, square_diff(start, end))

    def test_100(self):
        start = 1
        end = 100
        expected = 25164150
        self.assertEqual(expected, square_diff(start, end))


if __name__ == '__main__':
    unittest.main()
