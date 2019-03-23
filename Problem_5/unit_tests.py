import unittest
from problem_5 import smallest_multiple


class MyTestCase(unittest.TestCase):
    def test_basic(self):
        start = 1
        end = 10
        expected = 2520
        self.assertEqual(expected, smallest_multiple(start, end))


if __name__ == '__main__':
    unittest.main()
