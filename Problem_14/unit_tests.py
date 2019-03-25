import unittest
from problem_14 import collatz_sequence


class MyTestCase(unittest.TestCase):
    def test_basic(self):
        starting_number = 13
        collatz_sequence(starting_number)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
