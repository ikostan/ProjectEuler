#!/usr/bin/python


import unittest
import os
from Problems_1_to_100.Problem_21.problem_21 import sum_of_proper_divisors, \
    sum_of_amicable_numbers


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_sum_of_proper_divisors_220(self):
        number = 220
        expected = 284
        self.assertEqual(expected, sum_of_proper_divisors(number))

    def test_sum_of_proper_divisors_284(self):
        number = 284
        expected = 220
        self.assertEqual(expected, sum_of_proper_divisors(number))

    def test_sum_of_amicable_numbers_30(self):
        number = 30
        expected = 0
        self.assertEqual(expected, sum_of_amicable_numbers(number))

    def test_sum_of_amicable_numbers_300(self):
        number = 300
        expected = (220 + 284)
        self.assertEqual(expected, sum_of_amicable_numbers(number))

    def test_sum_of_amicable_numbers_10000(self):
        number = 10000
        expected = 31626
        self.assertEqual(expected, sum_of_amicable_numbers(number))


if __name__ == '__main__':
    unittest.main()
