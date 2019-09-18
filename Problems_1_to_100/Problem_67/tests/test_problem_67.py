#!/usr/bin/python

import unittest
import os
from Problems_1_to_100.Problem_67.problem_67 \
    import find_maximum_total
from Problems_1_to_100.Problem_67.problem_67 \
    import file_reader


class MyTestCase(unittest.TestCase):
    print("Running unit tests from: " +
          os.path.basename(__file__) + "\n")

    def test_basic(self):
        triangle = [[3],
                    [7, 4],
                    [2, 4, 6],
                    [8, 5, 9, 3]]

        expected = sum([3, 7, 4, 9])
        self.assertEqual(expected,
                         find_maximum_total(triangle))

    def test_basic_2(self):
        triangle = [[5],
                    [9, 6],
                    [4, 6, 8],
                    [0, 7, 1, 5]]

        expected = sum([5, 9, 6, 7])
        self.assertEqual(expected,
                         find_maximum_total(triangle))

    def test_big(self):
        triangle = [[75],
                    [95, 64],
                    [17, 47, 82],
                    [18, 35, 87, 10],
                    [20, 4, 82, 47, 65],
                    [19, 1, 23, 75, 3, 34],
                    [88, 2, 77, 73, 7, 63, 67],
                    [99, 65, 4, 28, 6, 16, 70, 92],
                    [41, 41, 26, 56, 83, 40, 80, 70, 33],
                    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
                    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
                    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
                    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
                    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
                    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

        expected = sum([75, 64, 82, 87, 82, 75, 73,
                        28, 83, 32, 91, 78, 58, 73, 93])
        self.assertEqual(expected, find_maximum_total(triangle))

    def test_huge(self):
        triangle = file_reader()

        expected = 7273
        self.assertEqual(expected, find_maximum_total(triangle))
