import unittest
from problem_7 import prime_generator


class MyTestCase(unittest.TestCase):

    def test_basic(self):
        limit = 6
        expected = 13
        self.assertEqual(expected, prime_generator(limit))

    def test_10001(self):
        limit = 10001
        expected = 104743
        self.assertEqual(expected, prime_generator(limit))


if __name__ == '__main__':
    unittest.main()