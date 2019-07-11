#!/usr/bin/python


import unittest
import os
from Problems_1_to_100.Problem_27.problem_27 import main


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_sample(self):
        expected = 0
        max_n = 1000
        self.assertEqual(expected, main(max_n)['max'])

