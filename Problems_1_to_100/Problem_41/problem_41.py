#!/usr/bin/python


from utils.utils import print_time_log, is_pandigital, is_prime, primes_generator_iterable
import time


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
    primes = primes_generator_iterable(number, -1)

    while True:
        number = next(primes)
        if is_pandigital(number):
            print_time_log(start_time, number)
            return number
