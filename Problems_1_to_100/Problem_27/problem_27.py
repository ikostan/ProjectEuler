#!/usr/bin/python


from utils.utils import print_time_log, is_prime
import time


def main(max_n: int):

    start_time = time.time()
    a = 0
    max_primes = {'max': 0,
                  'a': 0,
                  'b': 0,
                  'n': 0,
                  'product': 0}

    while a <= 999:
        b = 0
        while b < 1000:
            primes = set()
            n = 0
            while n < max_n:
                temp = n ** 2 + a * n + b
                if is_prime(temp):
                    primes.add(temp)
                n += 1
            b += 1

        if max_primes['max'] < len(primes):
            max_primes['max'] = len(primes)
            max_primes['a'] = a
            max_primes['b'] = b
            max_primes['n'] = n
            max_primes['product'] = a * b
            print(max_primes)

        a += 1

    print_time_log(start_time, max_primes)
    return max_primes
