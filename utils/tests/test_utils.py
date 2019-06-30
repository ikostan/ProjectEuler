#!/usr/bin/python


import unittest.mock
import platform
import os
import io
import time
from utils.utils import print_time_log, get_full_path, is_prime, is_palindrome, convert_to_binary


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_time_log_less_than_minute(self, mock_stdout):

        start_time = time.time()
        time.sleep(15)
        end_time = time.time() - start_time
        print_time_log(start_time)
        captured = mock_stdout.getvalue().replace('\n', '')
        expected = "The answer {0} returned in {1} seconds".format('', int(round(end_time, 3)))
        self.assertEqual(expected, captured)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_time_log_more_than_minute(self, mock_stdout):

        answer = 1000
        start_time = time.time()
        time.sleep(65)
        end_time = time.time() - start_time
        print_time_log(start_time, answer)
        captured = mock_stdout.getvalue().replace('\n', '')
        expected = "The answer {0} returned in {1} minutes and {2} seconds".format(
            answer, int(end_time // 60), round(end_time % 60, 3))
        self.assertEqual(expected, captured)

    def test_get_full_path_windows_target_os(self):
        target_os = 'Windows'
        folder_name = '/utils/tests'
        file_name = 'test.txt'
        expected = os.getcwd() + '\\test.txt'

        if platform.system() == 'Linux':
            expected = '/home/travis/build/ikostan/ProjectEuler\\test.txt'

        self.assertEqual(expected, get_full_path(folder_name, file_name, target_os))

    # @unittest.skip("Automation test runs on Linux machine")
    def test_get_full_path_windows(self):
        folder_name = '/utils/tests'
        file_name = 'test.txt'
        expected = os.getcwd() + '\\test.txt'

        if platform.system() == 'Linux':
            expected = '/home/travis/build/ikostan/ProjectEuler/utils/tests/test.txt'

        self.assertEqual(expected, get_full_path(folder_name, file_name))

    def test_get_full_path_linux(self):
        target_os = 'Linux'
        folder_name = '/utils/tests'
        file_name = 'test.txt'
        expected = '/home/travis/build/ikostan/ProjectEuler/utils/tests/test.txt'

        if platform.system() == 'Windows':
            expected = os.getcwd() + '/utils/tests' + '/test.txt'

        self.assertEqual(expected, get_full_path(folder_name, file_name, target_os))

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


if __name__ == '__main__':
    unittest.main()
