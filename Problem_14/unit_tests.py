import unittest
from problem_14 import collatz_sequence
from problem_14 import get_max_counter
from problem_14 import get_collatz_counter


class MyTestCase(unittest.TestCase):

    def test_get_collatz_counter_13(self):
        starting_number = 13
        expected = 10
        self.assertEqual(expected, get_collatz_counter(starting_number))

    def test_get_collatz_counter_9(self):
        starting_number = 9
        expected = 20
        self.assertEqual(expected, get_collatz_counter(starting_number))

    def test_collatz_sequence_13(self):
        starting_number = 13
        collatz_sequence(starting_number)
        self.assertEqual(True, True)

    def test_collatz_sequence_9(self):
        starting_number = 9
        collatz_sequence(starting_number)
        self.assertEqual(True, True)

    def test_basic(self):
        starting_number = 13
        expected = 9
        self.assertEqual(expected, get_max_counter(starting_number)['number'])

    def test_large(self):
        starting_number = 999999
        expected = 837799
        self.assertEqual(expected, get_max_counter(starting_number)['number'])


if __name__ == '__main__':
    unittest.main()
