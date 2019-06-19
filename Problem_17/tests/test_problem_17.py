#!/usr/bin/python


import unittest
import os
from Problem_17.problem_17 import number_to_words_counter


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_basic(self):
        start = 1
        end = 5
        numbers = list(range(start, end + 1))
        expected = 19
        self.assertEqual(expected, number_to_words_counter(numbers))

    def test_medium(self):
        start = 1
        end = 100
        numbers = list(range(start, end + 1))
        expected = 864
        self.assertEqual(expected, number_to_words_counter(numbers))

    def test_big(self):
        start = 100
        end = 350
        numbers = list(range(start, end + 1))
        expected = 5453
        self.assertEqual(expected, number_to_words_counter(numbers))

    def test_large(self):
        start = 1
        end = 1000
        numbers = list(range(start, end + 1))
        expected = 21124
        self.assertEqual(expected, number_to_words_counter(numbers))


if __name__ == '__main__':
    unittest.main()
