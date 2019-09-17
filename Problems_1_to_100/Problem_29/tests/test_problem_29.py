#!/usr/bin/python

import os
import unittest
from Problems_1_to_100.Problem_29.problem_29 import generate_terms


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_generate_terms_basic(self):

        start = 2
        end = 5
        expected_terms = len([4, 8, 9, 16, 25, 27, 32, 64, 81,
                              125, 243, 256, 625, 1024, 3125])

        self.assertEqual(expected_terms,
                         len(generate_terms(start, end)))

    def test_generate_terms_large(self):
        start = 2
        end = 100
        expected_terms = 9183
        self.assertEqual(expected_terms,
                         len(generate_terms(start, end)))
