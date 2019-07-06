#!/usr/bin/python


import unittest
import os
from Problems_1_to_100.Problem_43.problem_43 import main, has_property


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_has_property_true(self):

        number = 1406357289
        self.assertTrue(has_property(number))

    def test_has_property(self):

        numbers = [1430952867, 1460357289, 1406357289, 4130952867, 4160357289, 4106357289]
        results = list()
        for number in numbers:
            results.append(has_property(number))
        self.assertTrue(all(results))

    def test_has_property_false(self):

        number = 1406357299
        self.assertFalse(has_property(number))

    def test_main(self):

        expected = 16695334890
        self.assertEqual(expected, main())


if __name__ == '__main__':
    unittest.main()
