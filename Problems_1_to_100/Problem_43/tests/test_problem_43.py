#!/usr/bin/python


import unittest
import os
from Problems_1_to_100.Problem_43 import *


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_sample(self):
        pass


if __name__ == '__main__':
    unittest.main()
