#!/usr/bin/python


import unittest
import os
from Problem_32.problem_32 import sum_of_all_products


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_sum_of_all_products(self):
        limit = 987654321
        expected = 0
        self.assertEqual(expected, sum_of_all_products(limit))


if __name__ == '__main__':
    unittest.main()
