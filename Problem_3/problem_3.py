#!/usr/bin/python

import time
import math


def get_largest_factor(number):
    start_time = time.time()

    results = factor(number)
    result = results[-1]

    print("result {0} returned in {1} seconds".format(result, time.time() - start_time))
    return result


def factor(number):
    result = list()

    if number == 2:
        result.append(number)
        return result

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0 and is_prime(i):
            result.append(i)

    return result


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

