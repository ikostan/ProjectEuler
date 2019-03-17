#!/usr/bin/python

import time


def get_largest_prime(number):
    start_time = time.time()
    result = max(find_prime_numbers(number))
    print("result {0} returned in {1} seconds".format(result, time.time() - start_time))
    return result


def find_prime_numbers(number):
    prime_numbers = list()
    for i in range(2, number):
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers


def is_prime(i):
    for n in range(2, i):
        if i % n == 0:
            return False
    return True

