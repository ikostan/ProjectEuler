#!/usr/bin/python


import time
import platform
import os
import math


# This function is used for logging processing time only
# Shows how long it took in order to get the answer
def print_time_log(start_time: time, result=''):

    end_time = time.time() - start_time

    if end_time < 60:
        print("The answer {0} returned in {1} seconds".format(
            result, round(end_time), 3))
    else:
        minutes = int(end_time / 60)
        seconds = end_time - (minutes * 60)
        print("The answer {0} returned in {1} minutes and {2} seconds".format(result, minutes, round(seconds, 3)))


# Returns full path based on differences between Linux and Windows
def get_full_path(file_folder: str, file_name: str, target_os=''):
    file_path = ''

    if target_os == '':
        target_os = platform.system()

    if target_os == 'Linux':
        file_path = os.getcwd() + file_folder + '/' + file_name  # linux
    elif target_os == 'Windows':
        file_path = os.getcwd() + '\\' + file_name  # windows
    # elif target_os == 'Darwin':
        # file_path = os.getcwd() + '/Problem_19/tests/leap_years.txt'  # MacOS
    return file_path


def is_prime(i):
    # Return TRUE if i is prime number. False otherwise
    if i == 2:
        return True

    if i > 2 and i % 2 == 0:
        return False

    for n in range(3, int(math.sqrt(i)) + 1, 2):
        if i % n == 0:
            return False

    return True


def is_palindrome(number: int):
    # convert a number to string
    word = str(number)
    # reverse string and compare to itself
    if word == word[::-1]:
        return True
    return False
