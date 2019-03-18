import unittest
from problem_4 import is_palindrome


class MyTestCase(unittest.TestCase):

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
