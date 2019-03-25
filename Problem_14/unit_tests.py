import unittest
from problem_14 import collatz_sequence
from problem_14 import get_max_counter
from problem_14 import get_collatz_counter


class MyTestCase(unittest.TestCase):

    def test_get_collatz_counter_13(self):
        starting_number = 13
        expected = 10  # expected sequence size
        self.assertEqual(expected, get_collatz_counter(starting_number))

    def test_get_collatz_counter_9(self):
        starting_number = 9
        expected = 20  # expected sequence size
        self.assertEqual(expected, get_collatz_counter(starting_number))

    def test_collatz_sequence_13(self):
        starting_number = 13
        expected = 10  # expected sequence size
        self.assertEqual(expected, collatz_sequence(starting_number))

    def test_collatz_sequence_9(self):
        starting_number = 9
        expected = 20  # expected sequence size
        self.assertEqual(expected, collatz_sequence(starting_number))

    def test_basic(self):
        starting_number = 13
        expected = 9  # the starting number that has biggest Collatz chain
        self.assertEqual(expected, get_max_counter(starting_number)['number'])

    def test_large(self):
        starting_number = 999999
        expected = 837799  # the starting number that has biggest Collatz chain
        self.assertEqual(expected, get_max_counter(starting_number)['number'])


if __name__ == '__main__':
    unittest.main()
