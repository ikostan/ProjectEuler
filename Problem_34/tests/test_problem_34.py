#!/usr/bin/python


import unittest
import os
from Problem_34.problem_34 import sum_of_factorials, is_equal, main


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_sum_of_factorials_basic(self):
        number = 145
        self.assertEqual(number, sum_of_factorials(number))

    def test_sum_is_equal_basic(self):
        number = 145
        self.assertEqual(True, is_equal(number))

    def test_main(self):
        result = 40730
        max_number = 41000
        self.assertEqual(result, main(max_number))


if __name__ == '__main__':
    unittest.main()
