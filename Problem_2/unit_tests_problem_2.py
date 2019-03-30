#!/usr/bin/python


import unittest
import os
from Problem_2.problem_2 import find_even_fibonacci


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_basic(self):
        max_num = 4000000
        expected = 4613732
        self.assertEqual(expected, find_even_fibonacci(max_num))


if __name__ == '__main__':
    unittest.main()
