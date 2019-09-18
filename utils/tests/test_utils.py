#!/usr/bin/python

import unittest.mock
import platform
import os
import io
import time
from utils.utils import print_time_log, get_full_path, is_prime, \
                        is_palindrome, convert_to_binary, primes_generator, \
                        primes_generator_iterable, is_pandigital, \
                        calc_triangular_number, calc_pentagonal_number, \
                        pentagonal_number_generator, is_pentagonal, \
                        triangular_number_generator, is_triangular


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " +
          os.path.basename(__file__) + "\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_time_log_less_than_minute(self, mock_stdout):

        start_time = time.time()
        time.sleep(15)
        end_time = time.time() - start_time
        print_time_log(start_time)
        captured = mock_stdout.getvalue().replace('\n', '')
        expected = "The answer {0} " \
                   "returned in {1} seconds".format('',
                                                    int(round(end_time, 3)))
        self.assertEqual(expected, captured)

    @unittest.skip("Fails on python 3.5")
    @unittest.mock.patch('sys.stdout',
                         new_callable=io.StringIO)
    def test_print_time_log_more_than_minute(self, mock_stdout):

        answer = 1000
        start_time = time.time()
        time.sleep(65)
        end_time = time.time() - start_time
        print_time_log(start_time, answer)
        captured = mock_stdout.getvalue().replace('\n', '')
        expected = "The answer {0} " \
                   "returned in {1} " \
                   "minutes and {2} " \
                   "seconds".format(
            answer, int(end_time // 60), round(end_time % 60, 3))
        self.assertEqual(expected, captured)

    def test_get_full_path_windows_target_os(self):
        target_os = 'Windows'
        folder_name = '/utils/tests'
        file_name = 'test.txt'
        expected = os.getcwd() + '\\test.txt'

        if platform.system() == 'Linux':
            expected = ['/home/travis/build/ikostan/ProjectEuler\\test.txt',
                        '/home/circleci/project\\test.txt']

        self.assertTrue(get_full_path(folder_name, file_name, target_os) in expected)

    # @unittest.skip("Automation test runs on Linux machine")
    def test_get_full_path_windows(self):
        folder_name = '/utils/tests'
        file_name = 'test.txt'
        expected = os.getcwd() + '\\test.txt'

        if platform.system() == 'Linux':
            expected = ['/home/travis/build/ikostan/ProjectEuler/utils/tests/test.txt',
                        '/home/circleci/project/utils/tests/test.txt']

        self.assertTrue(get_full_path(folder_name,
                                      file_name) in expected)

    def test_get_full_path_linux(self):
        target_os = 'Linux'
        folder_name = '/utils/tests'
        file_name = 'test.txt'
        expected = ['/home/travis/build/ikostan/ProjectEuler/utils/tests/test.txt',
                    '/home/circleci/project/utils/tests/test.txt']

        if platform.system() == 'Windows':
            expected = os.getcwd() + '/utils/tests' + '/test.txt'

        self.assertTrue(get_full_path(folder_name, file_name,
                                      target_os) in expected)

    def test_is_prime_2(self):
        self.assertEqual(True, is_prime(2))

    def test_is_prime_4(self):
        self.assertEqual(False, is_prime(4))

    def test_is_palindrome_6_digits(self):
        number = 906609
        self.assertEqual(True, is_palindrome(number))

    def test_is_palindrome_basic(self):
        number = 9009
        self.assertEqual(True, is_palindrome(number))

    def test_is_palindrome_negative(self):
        number = 9007
        self.assertEqual(False, is_palindrome(number))

    def test_is_palindrome_5_digits(self):
        number = 90709
        self.assertEqual(True, is_palindrome(number))

    def test_is_palindrome_5_digits_negative(self):
        number = 90705
        self.assertEqual(False, is_palindrome(number))

    def test_convert_to_binary(self):
        decimal = 585
        expected = '1001001001'
        self.assertEqual(expected, convert_to_binary(decimal))

    def test_primes_generator(self):

        limit = 30
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertListEqual(expected, primes_generator(limit))

    def test_primes_generator_iterable(self):

        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        result = list()
        primes = primes_generator_iterable(2)

        while len(result) != len(expected):
            result.append(next(primes))

        self.assertListEqual(expected, result)

    def test_is_pandigital_true(self):
        self.assertTrue(is_pandigital(15234))

    def test_is_pandigital_false(self):
        self.assertFalse(is_pandigital(15224))

    def test_is_pandigital_large_true(self):
        self.assertTrue(is_pandigital(1023456978))

    def test_is_pandigital_large_false(self):
        self.assertFalse(is_pandigital(10523456978))

    def test_calc_triangular_number(self):
        triangle_numbers = {0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55}
        results = set()
        n = 0
        while 55 not in results:
            results.add(calc_triangular_number(n))
            n += 1
        self.assertSetEqual(triangle_numbers, results)

    def test_is_triangular_true(self):

        triangle_numbers = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        results = list()
        for n in triangle_numbers:
            results.append(is_triangular(n))
        self.assertTrue(all(results))

    def test_is_triangular_false(self):

        triangle_numbers = [2, 4, 5, 11, 16, 22, 27, 37, 46, 56]
        results = list()
        for n in triangle_numbers:
            results.append(is_triangular(n))
        self.assertFalse(all(results))

    def test_triangular_number_generator(self):

        triangular_numbers = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        results = list()
        n = 0
        generator = triangular_number_generator(n)
        while len(results) != len(triangular_numbers):
            results.append(next(generator))
        self.assertListEqual(triangular_numbers, results)

    def test_calc_pentagonal_number(self):
        """
        The first ten pentagonal numbers are:
        1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
        :return:
        """

        pentagonal_numbers = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
        results = list()
        for n in range(1, len(pentagonal_numbers) + 1):
            results.append(calc_pentagonal_number(n))
        self.assertListEqual(pentagonal_numbers, results)

    def test_pentagonal_number_generator(self):

        expected = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
        result = list()
        generator = pentagonal_number_generator()

        while len(expected) != len(result):
            result.append(next(generator))

        self.assertListEqual(expected, result)

    def test_is_pentagonal_true(self):

        pentagonals = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
        results = list()

        for p in pentagonals:
            results.append(is_pentagonal(p))

        self.assertTrue(all(results))

    def test_is_pentagonal_false(self):

        pentagonals = [2, 4, 11, 20, 33, 57, 75, 90, 118, 141]
        results = list()

        for p in pentagonals:
            results.append(is_pentagonal(p))

        self.assertFalse(all(results))
