#!/usr/bin/python


import unittest
import os
from Problem_37.problem_37 import find_truncatable_primes


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_find_truncatable_primes(self):
        limit = 11
        expected = 0
        self.assertEqual(expected, find_truncatable_primes(limit))


if __name__ == '__main__':
    unittest.main()
