#!/usr/bin/python

import time
import math
from utils.utils import print_time_log, is_prime


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
