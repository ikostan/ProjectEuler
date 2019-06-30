#!/usr/bin/python


from utils.utils import print_time_log, is_prime
import time


def get_rotations(digit: int):
    '''
    The number, 197 has following rotations of the digits: 197, 971, and 719

    :param digit:
    :return rotations:
    '''

    rotations = set()
    rotations.add(digit)
    digits = [d for d in str(digit)]

    for n in range(1, len(digits)):

        temp = []
        for i, d in enumerate(digits):
            temp.append(digits[i - 1])

        digits = temp
        rotation = int(''.join(digits))
        rotations.add(rotation)

    return rotations


def is_circular(digit: int, debug=False):
    '''
    The number, 197, is called a circular prime
    because all rotations of the digits: 197, 971, and 719,
    are themselves prime.

    :param digit:
    :param debug:
    :return:
    '''

    results = list()
    combinations = get_rotations(digit)

    for digit in combinations:
        result = is_prime(digit)
        if result and debug:
            print('result: {0}, digit: {1}'.format(result, digit))
        results.append(result)

    return all(results)


def is_circular_pattern(digit: int):
    '''
    Circular primes:

    2, 3, 5, 7, 13, 17, 37, 79,
    113, 197, 199, 337, 1193, 3779,
    11939, 19937, 193939, 199933

    :param digit:
    :return:
    '''

    pattern = '1379'

    if len(str(digit)) > 1:
        for d in str(digit):
            if d not in pattern:
                return False

    return True


def main(max_limit: int):

    start_time = time.time()
    circulars = set()
    primes = [n for n in range(1, max_limit, 2) if is_prime(n) and is_circular_pattern(n)]
    # print('Finished with calculating prime numbers: {}'.format(time.time() - start_time))

    for n in primes:
        if n not in circulars and is_circular(n):
            for p in get_rotations(n):
                circulars.add(p)

    # print(sorted(circulars))
    result = len(circulars)
    print_time_log(start_time, result)
    return result
