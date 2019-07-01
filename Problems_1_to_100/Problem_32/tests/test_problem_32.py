#!/usr/bin/python


import unittest
import os
from Problems_1_to_100.Problem_32.problem_32 import sum_of_all_products


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_sum_of_all_products(self):
        limit = 987654321
        expected = 45228
        self.assertEqual(expected, sum_of_all_products(limit))


if __name__ == '__main__':
    unittest.main()
