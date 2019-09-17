#!/usr/bin/python

import time
from utils.utils import print_time_log, primes_generator


def get_sum(limit: int):

    start_time = time.time()
    primes = primes_generator(limit)
    result = sum(primes)
    print_time_log(start_time, result)
    return result
