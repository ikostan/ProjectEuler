#!/usr/bin/python

import time
import math
from utils.utils import print_time_log


def get_largest_factor(number):

    start_time = time.time()
    results = factor(number)
    result = results[-1]

    print_time_log(start_time, result)
    return result


def factor(number):
    result = list()

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

