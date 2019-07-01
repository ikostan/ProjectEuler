#!/usr/bin/python


import time
from utils.utils import is_prime
from utils.utils import print_time_log


def prime_generator(limit: int):
    start_time = time.time()
    primes = list()
    n = 2

    while len(primes) < limit:
        if is_prime(n):
            primes.append(n)
        n += 1

    print_time_log(start_time, primes[limit - 1])
    return primes[limit - 1]
