#!/usr/bin/python


import unittest
import os
from Problems_1_to_100.Problem_25.problem_25 import find_term


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_basic(self):

        number = [0, 1]
        counter = 1
        length = 3
        expected = 12
        self.assertEqual(expected, find_term(number, counter, length))

    def test_large(self):

        number = [0, 1]
        counter = 1
        length = 1000
        expected = 4782
        self.assertEqual(expected, find_term(number, counter, length))


if __name__ == '__main__':
    unittest.main()
