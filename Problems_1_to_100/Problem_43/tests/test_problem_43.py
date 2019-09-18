#!/usr/bin/python

import unittest
import os
from Problems_1_to_100.Problem_43.problem_43 \
    import main, has_sub_string_divisibility


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " +
          os.path.basename(__file__) + "\n")

    def test_has_property_true(self):

        number = [1, 4, 0, 6, 3, 5, 7, 2, 8, 9]
        self.assertTrue(has_sub_string_divisibility(number))

    def test_has_property(self):

        numbers = [[1, 4, 3, 0, 9, 5, 2, 8, 6, 7],
                   [1, 4, 6, 0, 3, 5, 7, 2, 8, 9],
                   [1, 4, 0, 6, 3, 5, 7, 2, 8, 9],
                   [4, 1, 3, 0, 9, 5, 2, 8, 6, 7],
                   [4, 1, 6, 0, 3, 5, 7, 2, 8, 9],
                   [4, 1, 0, 6, 3, 5, 7, 2, 8, 9]]

        results = list()
        for number in numbers:
            results.append(has_sub_string_divisibility(number))

        self.assertTrue(all(results))

    def test_has_property_false(self):

        number = [1, 4, 0, 7, 2, 6, 3, 5, 9, 9]
        self.assertFalse(has_sub_string_divisibility(number))

    def test_main(self):

        expected = 16695334890
        self.assertEqual(expected, main())
