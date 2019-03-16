import unittest
from problem_2 import find_even_fibonacci


class MyTestCase(unittest.TestCase):
    def test_basic(self):
        max_num = 4000000
        expected = 4613732
        self.assertEqual(expected, find_even_fibonacci(max_num))


if __name__ == '__main__':
    unittest.main()
