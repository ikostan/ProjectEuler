#!/usr/bin/python


import unittest
import os
from Problem_99.problem_99 import get_max_number


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_get_max_number(self):
        expected = 0
        self.assertEqual(expected, get_max_number())


if __name__ == '__main__':
    unittest.main()
