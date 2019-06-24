#!/usr/bin/python


import unittest
import os
from Problem_19.date import Date
from Problem_19.calendar import Calendar
from Problem_19.problem_19 import main
import utils.utils as utils


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

        file_path = utils.get_full_path('/Problem_19', 'leap_years.txt')

        with open(file_path) as source:
            for line in source:
                cls.leap_years.append(int(line.strip()))

    def test_main_year_1904(self):
        expected = 1
        stop_date = Date(31, '', Calendar.month_name[11], 1904)
        current_date = Date(1, Calendar.week_days[4], Calendar.month_name[0], 1904)
        self.assertEqual(expected, main(stop_date, current_date))

    def test_main_year_1999(self):
        expected = 1
        stop_date = Date(31, '', Calendar.month_name[11], 1999)
        current_date = Date(1, Calendar.week_days[4], Calendar.month_name[0], 1999)
        self.assertEqual(expected, main(stop_date, current_date))

    def test_main_year_1998_1999(self):
        expected = 4
        stop_date = Date(31, '', Calendar.month_name[11], 1999)
        current_date = Date(1, Calendar.week_days[3], Calendar.month_name[0], 1998)
        self.assertEqual(expected, main(stop_date, current_date))

    def test_main(self):
        expected = 171
        stop_date = Date(31, '', Calendar.month_name[11], 2000)
        current_date = Date(1, Calendar.week_days[0], Calendar.month_name[0], 1900)
        self.assertEqual(expected, main(stop_date, current_date))

    def test_is_leap_true(self):
        #  A leap year occurs on any year evenly divisible by 4,
        #  but not on a century unless it is divisible by 400

        results = []
        for year in self.leap_years:
            results.append(Calendar.is_leap(year))

        self.assertEqual(True, all(results))

    def test_is_leap_false(self):
        #  A leap year occurs on any year evenly divisible by 4,
        #  but not on a century unless it is divisible by 400

        non_leap_years = [year for year in range(1800, 2400, 1) if year not in self.leap_years]
        results = []
        for year in non_leap_years:
            results.append(Calendar.is_leap(year))

        self.assertEqual(False, all(results))


if __name__ == '__main__':
    unittest.main()
