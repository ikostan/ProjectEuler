#!/usr/bin/python


import unittest
import os
from Problems_1_to_100.Problem_48 import find_last_ten_digits


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_basic(self):
        number = str(10405071317)
        expected = number[-10:]
        self.assertEqual(expected, find_last_ten_digits(1, 10))

    def test_large(self):
        expected = '9110846700'
        self.assertEqual(expected, find_last_ten_digits(1, 1000))


if __name__ == '__main__':
    unittest.main()
