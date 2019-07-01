#!/usr/bin/python


import unittest
import os
from Problems_1_to_100.Problem_99.problem_99 import get_largest_result_line_num, file_reader


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_get_largest_result_line_num(self):
        # The line with the largest number is 709
        expected = 709
        self.assertEqual(expected, get_largest_result_line_num(file_reader()))


if __name__ == '__main__':
    unittest.main()
