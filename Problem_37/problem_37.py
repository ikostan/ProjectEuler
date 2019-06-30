#!/usr/bin/python


from utils.utils import print_time_log, primes_generator_iterable, is_prime
import time


def is_truncatable(number: int):
    '''
    
    :param number:
    :return:
    '''

    str_number = str(number)
    index = 0

    # Left shift:
    while index < len(str_number):
        if not is_prime(int(str_number[index:])):
            return False

        index += 1

    # Right shift:
    index = len(str_number)
    while index > 0:
        if not is_prime(int(str_number[:index])):
            return False

        index -= 1

    # print('Next truncatable prime: {}'.format(number))  # debug only
    return True


def find_truncatable_primes(limit: int, start_from: int):
    '''

    The number 3797 has an interesting property.
    Being prime itself, it is possible to continuously
    remove digits from left to right, and remain prime at each stage:
    3797, 797, 97, and 7.
    Similarly we can work from right to left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable
    from left to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

    :return:
    '''

    start_time = time.time()
    truncatable = set()
    next_prime = primes_generator_iterable(start_from)

    while len(truncatable) < limit:

        prime = next(next_prime)
        if is_truncatable(prime):
            truncatable.add(prime)

    result = sum(truncatable)
    print_time_log(start_time, result)
    return result
