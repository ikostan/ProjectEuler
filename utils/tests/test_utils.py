#!/usr/bin/python


import unittest.mock
import platform
import os
import io
import time
from utils.utils import print_time_log
from utils.utils import get_full_path


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_time_log_less_than_minute(self, mock_stdout):
        start_time = time.time()
        end_time = time.time() - start_time
        print_time_log(end_time)
        captured = mock_stdout.getvalue().replace('\n', '')
        expected = "The answer {0} returned in {1} seconds".format('', end_time)
        self.assertEqual(expected, captured)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_time_log_more_than_minute(self, mock_stdout):
        end_time = 65.0
        answer = 1000
        print_time_log(end_time, answer)
        captured = mock_stdout.getvalue().replace('\n', '')
        expected = "The answer {0} returned in {1} minutes and {2} seconds".format(
            answer, 1, 5.0)
        self.assertEqual(expected, captured)

    def test_get_full_path_windows_target_os(self):
        target_os = 'Windows'
        folder_name = '/utils/tests'
        file_name = 'test.txt'
        expected = os.getcwd() + '\\test.txt'

        if platform.system() == 'Linux':
            expected = '/home/travis/build/ikostan/ProjectEuler\\test.txt'

        self.assertEqual(expected, get_full_path(folder_name, file_name, target_os))

    #@unittest.skip("Automation test runs on Linux machine")
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


if __name__ == '__main__':
    unittest.main()
