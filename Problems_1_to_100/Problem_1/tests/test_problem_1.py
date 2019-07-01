#!/usr/bin/python


import unittest
import os
from Problems_1_to_100.Problem_1.problem_1 import get_multiplies_of_3_and_5
from Problems_1_to_100.Problem_1.problem_1 import div_by_nums


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

    def test_div_by_nums_false(self):
        result = False
        num = 4
        nums = [3, 5, 7, 9, 10]
        self.assertEqual(result, div_by_nums(num, nums))

    def test_div_by_nums_true(self):
        result = True
        num = 16
        nums = [4, 3, 5]
        self.assertEqual(result, div_by_nums(num, nums))

    def test_div_by_nums_true2(self):
        result = True
        num = 16
        nums = [3, 5, 7, 4]
        self.assertEqual(result, div_by_nums(num, nums))

    def test_div_by_nums_true3(self):
        result = True
        num = 16
        nums = [3, 5, 10, 4, 7]
        self.assertEqual(result, div_by_nums(num, nums))


if __name__ == '__main__':
    unittest.main()

