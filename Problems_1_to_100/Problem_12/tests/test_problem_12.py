#!/usr/bin/python


import unittest
import os
from Problems_1_to_100.Problem_12.problem_12 import triangle_number_generator


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_triangle_number_generator(self):
        dividers = 5
        expected = 28
        self.assertEqual(expected,
                         triangle_number_generator(dividers)['triangle'])

    def test_50(self):
        dividers = 50
        expected = 25200
        self.assertEqual(expected,
                         triangle_number_generator(dividers)['triangle'])

    def test_100(self):
        dividers = 100
        expected = 73920
        self.assertEqual(expected,
                         triangle_number_generator(dividers)['triangle'])

    def test_150(self):
        dividers = 150
        expected = 749700
        self.assertEqual(expected, triangle_number_generator(dividers)['triangle'])

    def test_250(self):
        dividers = 250
        expected = 2162160
        self.assertEqual(expected,
                         triangle_number_generator(dividers)['triangle'])

    def test_500(self):
        dividers = 500
        expected = 76576500
        self.assertEqual(expected,
                         triangle_number_generator(dividers)['triangle'])
