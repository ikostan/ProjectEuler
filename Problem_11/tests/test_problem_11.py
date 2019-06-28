#!/usr/bin/python


import unittest
import os
from Problem_11.problem_11 import get_max_product
from Problem_11.problem_11 import process_columns
from Problem_11.problem_11 import process_rows
from Problem_11.problem_11 import process_diagonal_up_left
from Problem_11.problem_11 import process_diagonal_up_right
from Problem_11.problem_11 import process_diagonal_down_right
from Problem_11.problem_11 import process_diagonal_down_left


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_process_columns(self):
        data = [[1, 2, 3, 4, 5],
                [1, 2, 3, 4, 5],
                [2, 3, 4, 5, 6],
                [5, 6, 8, 9, 10],
                [1, 2, 3, 4, 5]]
        counter = 4
        expected = (5 * 5 * 6 * 10)
        self.assertEqual(expected, process_columns(data, counter))

    def test_process_rows(self):
        data = [[1, 2, 3, 4, 5],
                [1, 2, 3, 4, 5],
                [2, 3, 4, 5, 6],
                [5, 6, 8, 9, 10],
                [1, 2, 3, 4, 5]]
        counter = 4
        expected = (6 * 8 * 9 * 10)
        self.assertEqual(expected, process_rows(data, counter))

    def test_process_diagonal_up_left(self):
        data = [[1, 2, 3, 4, 5],
                [1, 2, 3, 4, 5],
                [2, 3, 4, 5, 6],
                [5, 6, 8, 9, 10],
                [1, 2, 3, 4, 5]]
        counter = 4
        expected = (5 * 9 * 4 * 2)
        self.assertEqual(expected, process_diagonal_up_left(data))

    def test_process_diagonal_up_right(self):
        data = [[1, 2, 3, 4, 5],
                [1, 2, 3, 4, 5],
                [2, 3, 4, 5, 6],
                [5, 6, 8, 9, 10],
                [1, 2, 3, 4, 5]]
        counter = 4
        expected = (6 * 4 * 4 * 5)
        self.assertEqual(expected, process_diagonal_up_right(data))

    def test_process_diagonal_down_right(self):
        data = [[1, 2, 3, 4, 5],
                [1, 2, 3, 4, 5],
                [2, 3, 4, 5, 6],
                [5, 6, 8, 9, 10],
                [1, 2, 3, 4, 5]]
        expected = (2 * 4 * 9 * 5)
        self.assertEqual(expected, process_diagonal_down_right(data))

    def test_process_diagonal_down_left(self):
        data = [[1, 2, 3, 4, 5],
                [1, 2, 3, 4, 5],
                [2, 3, 4, 5, 6],
                [5, 6, 8, 9, 10],
                [1, 2, 3, 4, 5]]
        counter = 4
        expected = (6 * 4 * 4 * 5)
        self.assertEqual(expected, process_diagonal_down_left(data))

    def test_main(self):
        grid = [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
                [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
                [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
                [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
                [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
                [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
                [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
                [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95],
                [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
                [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
                [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
                [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
                [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
                [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
                [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
                [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
                [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
                [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]

        expected = 70600674
        counter = 4

        self.assertEqual(expected, get_max_product(grid, counter))


if __name__ == '__main__':
    unittest.main()
