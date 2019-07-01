#!/usr/bin/python


import unittest
import os
from Problems_1_to_100.Problem_16.problem_16 import find_the_sum


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_basic(self):
        number = 2
        power = 15
        expected = 26
        self.assertEqual(expected, find_the_sum(number, power))

    def test_big(self):
        number = 2
        power = 1000
        expected = 1366
        self.assertEqual(expected, find_the_sum(number, power))


if __name__ == '__main__':
    unittest.main()
