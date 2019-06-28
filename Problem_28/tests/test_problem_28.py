#!/usr/bin/python


import unittest
import os
from Problem_28.problem_28 import calc_sum
from Problem_28.problem_28 import data_generator


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_data_generator_basic(self):

        data = [[21, 22, 23, 24, 25],
                [20, 7, 8, 9, 10],
                [19, 6, 1, 2, 11],
                [18, 5, 4, 3, 12],
                [17, 16, 15, 14, 13]]
        size = 5
        self.assertListEqual(data, data_generator(size))

    def test_calc_sum_basic(self):

        data = [[21, 22, 23, 24, 25],
                [20, 7, 8, 9, 10],
                [19, 6, 1, 2, 11],
                [18, 5, 4, 3, 12],
                [17, 16, 15, 14, 13]]
        expected = 101
        self.assertEqual(expected, calc_sum(data))


if __name__ == '__main__':
    unittest.main()
