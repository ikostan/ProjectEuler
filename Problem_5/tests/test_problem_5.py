#!/usr/bin/python


import unittest
import os
import io
import unittest.mock
import time
from Problem_5.problem_5 import smallest_multiple
from Problem_5.problem_5 import print_time_log


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_basic(self):
        start = 1
        end = 10
        expected = 2520
        self.assertEqual(expected, smallest_multiple(start, end))

    def test_from_1_to_20(self):
        start = 1
        end = 20
        expected = 232792560
        self.assertEqual(expected, smallest_multiple(start, end))

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
