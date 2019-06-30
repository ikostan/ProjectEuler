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
        if rotation not in rotations:
            rotations.add(rotation)
            # print(rotations)

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


def main(max_limit: int):

    start_time = time.time()
    circulars = set()
    primes = [n for n in range(2, max_limit) if is_prime(n)]
    # print('Finished with calculating prime numbers: {}'.format(time.time() - start_time))

    for n in primes:
        if n not in circulars and is_circular(n):
            for p in get_rotations(n):
                circulars.add(p)

    # print(sorted(circulars))
    result = len(circulars)
    print_time_log(start_time, result)
    return result
