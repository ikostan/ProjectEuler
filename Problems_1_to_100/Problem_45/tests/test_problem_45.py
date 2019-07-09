#!/usr/bin/python


import unittest
import os
from Problems_1_to_100.Problem_45.problem_45 import main


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_main(self):
        '''
        It can be verified that T285 = P165 = H143 = 40755.

        Every hexagonal number is a triangular number since: r(2r-1)=1/2(2r-1)[(2r-1)+1].
        Source: http://mathworld.wolfram.com/HexagonalNumber.html

        Every pentagonal number is 1/3 of a triangular number.
        Source: http://mathworld.wolfram.com/PentagonalNumber.html

        Therefore, index = 166
        :return:
        '''

        index = 166
        expected = 1533776805
        self.assertEqual(expected, main(index))
