#!/usr/bin/python


import unittest
import os
import platform
from Problem_19.date import Date
from Problem_19.problem_19 import is_leap
from Problem_19.problem_19 import main


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    @classmethod
    def setUpClass(cls):
        '''
        Get all leap years from the text file
        and organize them as an array
        :return:
        '''

        cls.leap_years = []

        file_path = ''
        if platform.system() == 'Linux':
            file_path = os.getcwd() + '/Problem_19/tests/leap_years.txt'  # linux
        elif platform.system() == 'Windows':
            file_path = os.getcwd() + '\\leap_years.txt'  # windows
        # elif platform.system() == 'Darwin':
        # file_path = os.getcwd() + '/Problem_19/tests/leap_years.txt'  # MacOS

        with open(file_path) as source:
            for line in source:
                cls.leap_years.append(int(line.strip()))

    def test_main(self):
        expected = 171
        self.assertEqual(expected, main())

    def test_is_leap_true(self):
        #  A leap year occurs on any year evenly divisible by 4,
        #  but not on a century unless it is divisible by 400

        results = []
        for year in self.leap_years:
            results.append(is_leap(year))

        self.assertEqual(True, all(results))

    def test_is_leap_false(self):
        #  A leap year occurs on any year evenly divisible by 4,
        #  but not on a century unless it is divisible by 400

        non_leap_years = [year for year in range(1800, 2400, 1) if year not in self.leap_years]
        results = []
        for year in non_leap_years:
            results.append(is_leap(year))

        self.assertEqual(False, all(results))


if __name__ == '__main__':
    unittest.main()
