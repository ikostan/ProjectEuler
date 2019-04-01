#!/usr/bin/python


import time
import math


def calc_lattice_path(width: int, height: int):
    start_time = time.time()
    head = multiply_members(list(range(max(width, height) + 1, width + height + 1)))

    if width == height:
        tail = multiply_members(list(range(1, max(width, height) + 1)))
    else:
        tail = multiply_members(list(range(1, min(width, height) + 1)))

    result = head / tail
    end_time = time.time() - start_time
    print_time_log(end_time, result)
    return result


def multiply_members(primes: list):
    print(primes)
    result = 1
    for n in primes:
        result *= n

    return result


def is_prime(n: int):
    if n == 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0 and n > 2:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


# This function is used for logging processing time only
# Shows how long it took in order to get the answer
def print_time_log(end_time: time, result):
    if end_time < 60:
        print("The answer {0} returned in {1} seconds".format(
            result, end_time))
    else:
        minutes = int(end_time / 60)
        seconds = end_time - (minutes * 60)
        print("The answer {0} returned in {1} minutes and {2} seconds".format(
            result, minutes, seconds))
