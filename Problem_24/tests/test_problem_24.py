#!/usr/bin/python


import unittest
import os
from Problem_24.problem_24 import lexicographic_permutations


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_lexicographic_permutation_short(self):

        index = 5
        numbers = [0, 1, 2]
        expected = 210
        self.assertEqual(expected, lexicographic_permutations(numbers, index))

    def test_lexicographic_permutation_large(self):

        index = 1000000 - 1
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = 2783915460
        self.assertEqual(expected, lexicographic_permutations(numbers, index))


if __name__ == '__main__':
    unittest.main()
