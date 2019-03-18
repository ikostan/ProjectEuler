import unittest
from problem_4 import is_palindrome


class MyTestCase(unittest.TestCase):

    def test_is_palindrome(self):
        number = 9009
        self.assertEqual(True, is_palindrome(number))


if __name__ == '__main__':
    unittest.main()
