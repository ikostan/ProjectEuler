#!/usr/bin/python


import unittest
import os
from Problem_4.problem_4 import is_palindrome
from Problem_4.problem_4 import large_palindrome_generator


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_large_palindrome_generator_basic(self):
        start = 10
        end = 99
        expected = 9009
        self.assertEqual(expected, large_palindrome_generator(start, end))

    def test_large_palindrome_generator_3_digits(self):
        start = 100
        end = 999
        expected = 906609
        self.assertEqual(expected, large_palindrome_generator(start, end))

    def test_is_palindrome_6_digits(self):
        number = 906609
        self.assertEqual(True, is_palindrome(number))

    def test_is_palindrome_basic(self):
        number = 9009
        self.assertEqual(True, is_palindrome(number))

    def test_is_palindrome_negative(self):
        number = 9007
        self.assertEqual(False, is_palindrome(number))

    def test_is_palindrome_5_digits(self):
        number = 90709
        self.assertEqual(True, is_palindrome(number))

    def test_is_palindrome_5_digits_negative(self):
        number = 90705
        self.assertEqual(False, is_palindrome(number))


if __name__ == '__main__':
    unittest.main()
