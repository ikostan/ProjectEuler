#!/usr/bin/python


import time
import math
from Template.problem_ import print_time_log


def prime_generator(limit: int):
    start_time = time.time()
    primes = list()
    n = 2

    while len(primes) < limit:
        if is_prime(n):
            primes.append(n)
        n += 1

    end_time = time.time() - start_time
    print_time_log(end_time, primes[limit - 1])
    return primes[limit - 1]


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
