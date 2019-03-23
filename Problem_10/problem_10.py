#!/usr/bin/python


import time
import math


def get_sum(limit: int):
    start_time = time.time()
    primes = primes_generator(limit)
    result = sum(primes)
    end_time = time.time() - start_time
    print_log(end_time, result)
    return result


def primes_generator(limit: int):
    primes = list()
    for i in range(2, limit):
        if is_prime(i):
            primes.append(i)
    return primes


def is_prime(n: int):

    if n == 1:
        return False

    if n == 2:
        return True

    if n > 2 and n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def print_log(end_time, result):
    if end_time < 60:
        print("The answer {0} returned in {1} seconds".format(result, end_time))
    else:
        minutes = int(end_time / 60)
        seconds = end_time - (minutes * 60)
        print("The answer {0} returned in {1} minutes and {2} seconds".format(result, minutes, seconds))