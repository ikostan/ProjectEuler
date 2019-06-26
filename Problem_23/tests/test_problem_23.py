#!/usr/bin/python


import unittest
import os
from Problem_23.problem_23 import is_abundant
from Problem_23.problem_23 import main
from Problem_23.problem_23 import sum_proper_divisors


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_get_proper_divisors_28(self):
        result = sum([1, 2, 4, 7, 14])
        number = 28
        self.assertEqual(result, sum_proper_divisors(number))

    def test_get_proper_divisors_12(self):
        result = sum([1, 2, 3, 4, 6])
        number = 12
        self.assertEqual(result, sum_proper_divisors(number))

    def test_check_abundant_large(self):
        numbers = [12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72,
                   78, 80, 84, 88, 90, 96, 100, 102, 104, 108, 112, 114, 120,
                   126, 132, 138, 140, 144, 150, 156, 160, 162, 168, 174, 176,
                   180, 186, 192, 196, 198, 200, 204, 208, 210, 216, 220, 222,
                   224, 228, 234, 240, 246, 252, 258, 260, 264, 270]
        expected = True
        results = []

        for n in numbers:
            results.append(is_abundant(n))

        self.assertEqual(expected, all(results))

    def test_main_long(self):
        upper_limit = 28123
        result = 4179871
        self.assertEqual(result, main(upper_limit))


if __name__ == '__main__':
    unittest.main()
