#!/usr/bin/python


import unittest
import os
from Problems_1_to_100.Problem_15 import calc_lattice_path


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_2_x_2(self):
        width = 2
        height = 2
        expected = 6
        self.assertEqual(expected, calc_lattice_path(width, height))

    def test_3_x_3(self):
        width = 3
        height = 3
        expected = 20
        self.assertEqual(expected, calc_lattice_path(width, height))

    def test_3_x_4(self):
        width = 3
        height = 4
        expected = 35
        self.assertEqual(expected, calc_lattice_path(width, height))

    def test_4_x_3(self):
        width = 4
        height = 3
        expected = 35
        self.assertEqual(expected, calc_lattice_path(width, height))

    def test_4_x_4(self):
        width = 4
        height = 4
        expected = 70
        self.assertEqual(expected, calc_lattice_path(width, height))

    def test_5_x_10(self):
        width = 5
        height = 10
        expected = 3003
        self.assertEqual(expected, calc_lattice_path(width, height))

    def test_5_x_15(self):
        width = 5
        height = 15
        expected = 15504
        self.assertEqual(expected, calc_lattice_path(width, height))

    def test_20_x_20(self):
        width = 20
        height = 20
        expected = 137846528820
        self.assertEqual(expected, calc_lattice_path(width, height))


if __name__ == '__main__':
    unittest.main()
