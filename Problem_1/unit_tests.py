#!/usr/bin/python


import unittest
from problem_1 import get_multiplies_of_3_and_5


class MyTestCase(unittest.TestCase):
    def test_basic(self):
        result = 23
        max_num = 10
        nums = [3, 5]
        self.assertEqual(result, get_multiplies_of_3_and_5(max_num, nums))

    def test_1000(self):
        result = 233168
        max_num = 1000
        nums = [3, 5]
        self.assertEqual(result, get_multiplies_of_3_and_5(max_num, nums))


if __name__ == '__main__':
    unittest.main()

