#!/usr/bin/python


import unittest
import os
from Problem_1.problem_1 import get_multiplies_of_3_and_5


class MyTestCase(unittest.TestCase):
    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_10(self):
        result = 23
        max_num = 10
        nums = [3, 5]
        self.assertEqual(result, get_multiplies_of_3_and_5(max_num, nums))

    def test_100(self):
        result = 2318
        max_num = 100
        nums = [3, 5]
        self.assertEqual(result, get_multiplies_of_3_and_5(max_num, nums))

    def test_1000(self):
        result = 233168
        max_num = 1000
        nums = [3, 5]
        self.assertEqual(result, get_multiplies_of_3_and_5(max_num, nums))


if __name__ == '__main__':
    unittest.main()

