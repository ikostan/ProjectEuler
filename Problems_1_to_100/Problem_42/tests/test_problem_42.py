#!/usr/bin/python


import unittest
import os
from Problems_1_to_100.Problem_42.problem_42 import main, \
    words_reader, \
    calc_word_number, \
    is_triangle, \
    generate_triangle_numbers


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    @classmethod
    def setUpClass(cls):
        cls.path = '/Problems_1_to_100/Problem_42/tests/'
        cls.file_name = 'p042_words.txt'
        cls.words = words_reader(cls.path, cls.file_name)
        cls.triangle_numbers = {0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66,
                                78, 91, 105, 120, 136, 153, 171, 190, 210, 231,
                                253, 276, 300, 325, 351, 378, 406, 435, 465, 496,
                                528, 561, 595, 630, 666, 703, 741, 780, 820, 861,
                                903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275,
                                1326, 1378, 1431}

    def test_main(self):
        expected = 162
        self.assertEqual(expected, main(self.words))

    def test_generate_triangle_numbers(self):
        results = []
        triangle_nums = generate_triangle_numbers(self.words)
        for t in triangle_nums:
            results.append(t in self.triangle_numbers)
        self.assertTrue(all(results))

    def test_calc_word_number(self):
        word = 'SKY'
        expected = 55
        self.assertEqual(expected, calc_word_number(word))

    def test_is_triangle(self):
        word = 'SKY'
        self.assertTrue(is_triangle(word, self.triangle_numbers))


if __name__ == '__main__':
    unittest.main()
