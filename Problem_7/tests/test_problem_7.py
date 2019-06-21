#!/usr/bin/python


import unittest
import os
from Problem_7.problem_7 import prime_generator
from Problem_7.problem_7 import is_prime


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_basic(self):
        limit = 6
        expected = 13
        self.assertEqual(expected, prime_generator(limit))

    def test_10001(self):
        limit = 10001
        expected = 104743
        self.assertEqual(expected, prime_generator(limit))

    def test_is_prime_1(self):
        self.assertEqual(False, is_prime(1))

    def test_is_prime_2(self):
        self.assertEqual(True, is_prime(2))


if __name__ == '__main__':
    unittest.main()
