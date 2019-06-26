#!/usr/bin/python


from utils.utils import print_time_log
import math
import time


def sum_proper_divisors(num: int):
    '''
    Calculates sum of all proper divisors
    :param num:
    :return:
    '''

    sum_divisors = 0
    for n in range(1, int(math.sqrt(num)) + 1):
        if num % n == 0:
            if num // n == n:
                sum_divisors += n
            else:
                sum_divisors += n + (num // n)

    # The sum not includes the number itself
    return sum_divisors - num


def is_abundant(num: int):
    '''
    A number n is called abundant if the sum
    of the proper divisors exceeds n.
    :param num:
    :return:
    '''
    if sum_proper_divisors(num) > num:
        return True
    return False


def main(upper_limit: int):
    start_time = time.time()
    result = 0

    # 1
    all_abundant = set()
    for n in range(1, upper_limit):
        if is_abundant(n):
            all_abundant.add(n)

    for a in range(1, upper_limit):
        result += a
        for b in all_abundant:
            c = a - b

            if c < 1:
                break

            if c in all_abundant:
                result -= a
                break

    print_time_log(time.time() - start_time, result)
    return result
