#!/usr/bin/python


from utils.utils import print_time_log, is_pandigital, is_prime
import time


def has_pandigital_pattern(digit: int):

    digit_str = str(digit)
    digit_set = set(int(d) for d in digit_str)
    return len(digit_set) == len(digit_str)


def find_largest_pandigital_prime(number: int):
    '''
    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once.
    For example, 2143 is a 4-digit pandigital and is also prime.
    What is the largest n-digit pandigital prime that exists?
    :param number:
    :return:
    '''

    start_time = time.time()

    for n in range(number, 1, -1):
        if is_pandigital(n) and is_prime(n):
            print_time_log(start_time, n)
            return n
