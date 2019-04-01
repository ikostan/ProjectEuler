#!/usr/bin/python


import unittest
import os
import math


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_basic(self):
        number = 2
        power = 15
        n = math.pow(number, power)
        numbers = (3, 2, 7, 6, 8)
        expected = 26
        self.assertEqual(expected, False)

    def test_big(self):
        number = 2
        power = 15
        expected = 26
        self.assertEqual(expected, False)


if __name__ == '__main__':
    unittest.main()
