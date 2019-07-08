#!/usr/bin/python


import unittest
import os
from Problems_1_to_100.Problem_44.problem_44 import main


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_main(self):
        '''
        The first ten pentagonal numbers are:
        1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

        Find the pair of pentagonal numbers, Pj and Pk,
        for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised;

        what is the value of D?
        :return:
        '''

        expected = 5482660
        self.assertEqual(expected, main())

