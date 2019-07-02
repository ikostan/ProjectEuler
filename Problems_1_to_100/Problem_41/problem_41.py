#!/usr/bin/python


from utils.utils import print_time_log, is_pandigital, is_prime
import time
import itertools


def find_largest_pandigital_prime(numbers: list):
    '''
    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once.
    For example, 2143 is a 4-digit pandigital and is also prime.
    What is the largest n-digit pandigital prime that exists?
    :param number:
    :return:
    '''

    start_time = time.time()
    permutations = list(
        int(''.join(t)) for t in itertools.permutations(str(t) for t in numbers))  # if t[0] != '0')

    big_pandigital_primes = set()
    for n in permutations:
        if is_pandigital(n) and is_prime(n):
            big_pandigital_primes.add(n)

    result = max(big_pandigital_primes)
    print_time_log(start_time, result)
    return result
