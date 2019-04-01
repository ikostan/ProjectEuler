#!/usr/bin/python


import unittest
import os
from Problem_17.problem_17 import number_to_words


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_basic(self):
        start = 1
        end = 5
        numbers = list(range(start, end + 1))
        expected = 19
        self.assertEqual(expected, len(number_to_words(numbers)))

    def test_big(self):
        start = 1
        end = 1000
        numbers = list(range(start, end + 1))
        expected = 19
        self.assertEqual(expected, len(number_to_words(numbers)))


if __name__ == '__main__':
    unittest.main()
