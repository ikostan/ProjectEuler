#!/usr/bin/python


import unittest.mock
import os
import io
import time
from Problem_6.problem_6 import print_time_log
from Problem_6.problem_6 import sum_squares_of_numbers
from Problem_6.problem_6 import square_of_sums
from Problem_6.problem_6 import square_diff


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_sum_of_squares(self):
        expected = 385
        start = 1
        end = 10
        self.assertEqual(expected, sum_squares_of_numbers(start, end))

    def test_square_of_sums(self):
        expected = 3025
        start = 1
        end = 10
        self.assertEqual(expected, square_of_sums(start, end))

    def test_basic(self):
        start = 1
        end = 10
        expected = 2640
        self.assertEqual(expected, square_diff(start, end))

    def test_100(self):
        start = 1
        end = 100
        expected = 25164150
        self.assertEqual(expected, square_diff(start, end))

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_time_log_less_than_minute(self, mock_stdout):
        start_time = time.time()
        end_time = time.time() - start_time
        print_time_log(end_time)
        captured = mock_stdout.getvalue().replace('\n', '')
        expected = "The answer {0} returned in {1} seconds".format('', end_time)
        self.assertEqual(expected, captured)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_time_log_more_than_minute(self, mock_stdout):
        end_time = 65.0
        answer = 1000
        print_time_log(end_time, answer)
        captured = mock_stdout.getvalue().replace('\n', '')
        expected = "The answer {0} returned in {1} minutes and {2} seconds".format(
            answer, 1, 5.0)
        self.assertEqual(expected, captured)

if __name__ == '__main__':
    unittest.main()
