#!/usr/bin/python


from utils.utils import print_time_log, is_prime
import time


def main():

    start_time = time.time()
    max_primes = {'max': 0,
                  'a': 0,
                  'b': 0,
                  'product': 0}

    for a in range(-40, 41, 1):
        for b in range(-41, 42, 1):
            n = 0
            primes = set()
            while n <= a:
                temp = quadratic_primes(a, b, n)
                if is_prime(temp):
                    primes.add(temp)
                a += 1

            temp_max = len(primes)
            if max_primes['max'] < temp_max:
                max_primes['max'] = temp_max
                max_primes['a'] = a
                max_primes['b'] = b
                max_primes['product'] = a * b
                print_primes(max_primes)

    print_time_log(start_time, max_primes['product'])
    return max_primes


def quadratic_primes(a, b, n):
    return n*n+a*n+b


def print_primes(max_primes: set):
    product = max_primes['a'] * max_primes['b']
    print('\nmax: {} -> {}, '
          'a: {} -> {}, '
          'b: {} -> {}, '
          'product: {} -> {}'.format(max_primes['max'],
                                     is_prime(max_primes['max']),
                                     max_primes['a'],
                                     is_prime(max_primes['a']),
                                     max_primes['b'],
                                     is_prime(max_primes['b']),
                                     product,
                                     is_prime(product)))
