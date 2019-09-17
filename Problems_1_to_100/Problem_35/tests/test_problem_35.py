#!/usr/bin/python

import unittest
import os
from Problems_1_to_100.Problem_35.problem_35 \
    import is_circular, get_rotations, main


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_get_rotations(self):
        """
        The number, 197, has following rotations of the digits:
        197, 971, and 719,
        are themselves prime.
        :return:
        """
        number = 197
        expected = {197, 971, 719}
        self.assertSetEqual(expected, get_rotations(number))

    def test_is_circular_true(self):
        """
        The number, 197, is called a circular prime
        because all rotations of the digits:
        197, 971, and 719,
        are themselves prime.
        :return:
        """
        number = 197
        self.assertEqual(True, is_circular(number, True))

    def test_is_circular_false(self):
        """
        The number, 197, is called a circular prime
        because all rotations of the digits:
        197, 971, and 719,
        are themselves prime.
        :return:
        """
        number = 196
        self.assertEqual(False, is_circular(number))

    def test_main_100(self):
        limit = 100
        expected = len([2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97])
        self.assertEqual(expected, main(limit))

    def test_main_1000000(self):
        limit = 1000000
        expected = 55
        self.assertEqual(expected, main(limit))
