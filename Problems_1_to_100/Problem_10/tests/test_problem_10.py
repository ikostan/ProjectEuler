#!/usr/bin/python


import unittest
import os
from Problems_1_to_100.Problem_10.problem_10 import get_sum


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_2000000(self):

        limit = 2000000
        expected = 142913828922
        self.assertEqual(expected, get_sum(limit))
