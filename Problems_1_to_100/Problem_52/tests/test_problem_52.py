#!/usr/bin/python


import unittest
import os
from Problems_1_to_100.Problem_52.problem_52 import main


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_main(self):
        number = 1
        expected = 142857
        self.assertEqual(expected, main(number))
