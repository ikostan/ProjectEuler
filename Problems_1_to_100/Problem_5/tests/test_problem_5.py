#!/usr/bin/python


import unittest
import os
from Problems_1_to_100.Problem_5.problem_5 import smallest_multiple


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_basic(self):
        start = 1
        end = 10
        expected = 2520
        self.assertEqual(expected, smallest_multiple(start, end))

    def test_from_1_to_20(self):
        start = 1
        end = 20
        expected = 232792560
        self.assertEqual(expected, smallest_multiple(start, end))


if __name__ == '__main__':
    unittest.main()
