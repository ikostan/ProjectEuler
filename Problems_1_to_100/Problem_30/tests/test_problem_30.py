#!/usr/bin/python

import unittest
import os
from Problems_1_to_100.Problem_30.problem_30 \
    import is_sum_of_powers_of_their_digits, main


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_is_sum_of_powers_of_their_digits_1634(self):
        power = 4
        digit = 1634
        self.assertEqual(True,
                         is_sum_of_powers_of_their_digits(digit, power))

    def test_is_sum_of_powers_of_their_digits_8208(self):
        power = 4
        digit = 8208
        self.assertEqual(True,
                         is_sum_of_powers_of_their_digits(digit, power))

    def test_is_sum_of_powers_of_their_digits_9474(self):
        power = 4
        digit = 9474
        self.assertEqual(True,
                         is_sum_of_powers_of_their_digits(digit, power))

    def test_main_basic(self):
        power = 4
        expected = 1634 + 8208 + 9474  # -> 19316
        self.assertEqual(expected,
                         main(power))

    def test_main(self):
        power = 5
        expected = 443839
        self.assertEqual(expected,
                         main(power))
