#!/usr/bin/python


import time
import platform
import os
import math


#TODO: each method must have his own .py file


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
    '''
    Return TRUE if i is prime number. False otherwise
    :param i:
    :return:
    '''

    if i == 1:
        return False

    if i == 2:
        return True

    if i > 2 and i % 2 == 0:
        return False

    for n in range(3, int(math.sqrt(i)) + 1, 2):
        if i % n == 0:
            return False

    return True


def primes_generator(limit: int, start=1):
    '''
    Generates list of prime numbers within specified limit
    :param limit:
    :param start:
    :return:
    '''

    primes = list()
    for i in range(start, limit):
        if is_prime(i):
            primes.append(i)
    return primes


def primes_generator_iterable(start: int, step=1):
    '''
    Generates list of prime numbers within specified limit
    :param step:
    :param start:
    :return:
    '''

    while True:
        if is_prime(start):
            yield start
        start += step


def is_palindrome(number: int):
    '''
    A palindrome is a word, number, phrase, or
    other sequence of characters which reads the same backward as forward,
    such as madam or racecar or the number 10801.
    :param number:
    :return:
    '''
    # convert a number to string
    word = str(number)
    # reverse string and compare to itself
    if word == word[::-1]:
        return True
    return False


def convert_to_binary(number: int):
    '''
    code for converting a decimal number to it’s binary equivalent
    :param number:
    :return:
    '''
    return bin(number).replace("0b", "")


def is_pandigital(digit: str):
    '''
    We shall say that an n-digit number is pandigital
    if it makes use of all the digits 1 to n exactly once;
    for example, the 5-digit number, 15234, is 1 through 5 pandigital.

    A number is said to be pandigital if it contains each of the digits
    from 0 to 9 (and whose leading digit must be nonzero).
    However, "zeroless" pandigital quantities contain the digits 1 through 9.
    Sometimes exclusivity is also required so that each digit is restricted
    to appear exactly once. For example, 6729/13458 is a (zeroless, restricted)
    pandigital fraction and 1023456789 is the smallest (zerofull) pandigital number.

    The first few zerofull restricted pandigital numbers are 1023456789, 1023456798,
    1023456879, 1023456897, 1023456978, ...

    :param digit:
    :return:
    '''

    digit_str = str(digit)
    digit_set = set(int(d) for d in digit_str)
    if len(digit_set) != len(digit_str):
        return False

    pattern = set(n for n in range(min(digit_set), max(digit_set) + 1))
    return digit_set == pattern
