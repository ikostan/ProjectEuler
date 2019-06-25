#!/usr/bin/python


import unittest
import os
from Problem_23.problem_23 import get_sum_of_proper_divisors
from Problem_23.problem_23 import define_number
from Problem_23.problem_23 import main
from Problem_23.problem_23 import check_abundant


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_get_proper_divisors_28(self):
        result = sum([1, 2, 4, 7, 14])
        number = 28
        self.assertEqual(result, get_sum_of_proper_divisors(number))

    def test_get_proper_divisors_12(self):
        result = sum([1, 2, 3, 4, 6])
        number = 12
        self.assertEqual(result, get_sum_of_proper_divisors(number))

    def test_define_number_perfect_28(self):
        result = 'perfect'
        number = 28
        self.assertEqual(result, define_number(number, get_sum_of_proper_divisors(number)))

    def test_define_number_perfect_large(self):
        numbers = [6, 28, 496, 8128]
        expected = True
        result = 'perfect'
        results = []

        for n in numbers:
            if define_number(n, get_sum_of_proper_divisors(n)) == result:
                results.append(True)
            else:
                results.append(False)

        self.assertEqual(expected, all(results))

    def test_define_number_abundant_12(self):
        result = 'abundant'
        number = 12
        self.assertEqual(result, define_number(number, get_sum_of_proper_divisors(number)))

    def test_define_number_abundant_large(self):
        numbers = [12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72,
                   78, 80, 84, 88, 90, 96, 100, 102, 104, 108, 112, 114, 120,
                   126, 132, 138, 140, 144, 150, 156, 160, 162, 168, 174, 176,
                   180, 186, 192, 196, 198, 200, 204, 208, 210, 216, 220, 222,
                   224, 228, 234, 240, 246, 252, 258, 260, 264, 270]
        expected = True
        result = 'abundant'
        results = []

        for n in numbers:
            if define_number(n, get_sum_of_proper_divisors(n)) == result:
                results.append(True)
            else:
                results.append(False)

        self.assertEqual(expected, all(results))

    def test_check_abundant_large(self):
        numbers = [12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72,
                   78, 80, 84, 88, 90, 96, 100, 102, 104, 108, 112, 114, 120,
                   126, 132, 138, 140, 144, 150, 156, 160, 162, 168, 174, 176,
                   180, 186, 192, 196, 198, 200, 204, 208, 210, 216, 220, 222,
                   224, 228, 234, 240, 246, 252, 258, 260, 264, 270]
        expected = True
        results = []

        for n in numbers:
            results.append(check_abundant(n))

        self.assertEqual(expected, all(results))

    def test_define_number_deficient_17(self):
        result = 'deficient'
        number = 17
        self.assertEqual(result, define_number(number, get_sum_of_proper_divisors(number)))

    def test_define_number_deficient_large(self):
        numbers = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 21, 22, 23]
        expected = True
        result = 'deficient'
        results = []

        for n in numbers:
            if define_number(n, get_sum_of_proper_divisors(n)) == result:
                results.append(True)
            else:
                results.append(False)

        self.assertEqual(expected, all(results))

    def test_check_abundant_vs_define_number(self):
        # all integers greater than 28123 can be written as the sum of two abundant numbers
        number = 28123
        result_1 = set()
        result_2 = set()

        for n in range(1, number + 1):

            if check_abundant(n):
                result_1.add(n)

            if define_number(n, get_sum_of_proper_divisors(n)) == 'abundant':
                result_2.add(n)

        self.assertSetEqual(result_1, result_2)

    @unittest.skip('This test takes too long')
    def test_main(self):
        upper_limit = 28123
        result = 4179871
        self.assertEqual(result, main(upper_limit))


if __name__ == '__main__':
    unittest.main()
