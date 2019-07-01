#!/usr/bin/python


import unittest
import string
import os
from Problems_1_to_100.Problem_22 import file_reader
from Problems_1_to_100.Problem_22 import alphabetical_value
from Problems_1_to_100.Problem_22 import total_of_all_name_scores


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_file_reader(self):
        # Test a 46K text file containing over five-thousand first names
        total_names_in_file = 5000
        self.assertEqual(True, len(file_reader()) > total_names_in_file)

    def test_alphabetical_value(self):
        name = 'COLIN'
        alphabet = string.ascii_uppercase
        expected = 3 + 15 + 12 + 9 + 14
        self.assertEqual(expected, alphabetical_value(name, alphabet))

    def test_total_of_all_name_scores(self):
        expected = 871198282
        self.assertEqual(expected, total_of_all_name_scores())

    def test_name_index(self):
        name = 'COLIN'
        expected = 938
        names = file_reader()
        self.assertEqual(expected, names.index(name) + 1)


if __name__ == '__main__':
    unittest.main()
