#!/usr/bin/python


import os
import unittest
from Problems_1_to_100.Problem_9.problem_9 import find_triplet


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_basic(self):
        a = 3
        b = 4
        c = 5
        num = a + b + c
        expected = a * b * c
        self.assertEqual(expected, find_triplet(num))

    def test_1000(self):
        num = 1000
        expected = 31875000
        self.assertEqual(expected, find_triplet(num))


if __name__ == '__main__':
    unittest.main()
