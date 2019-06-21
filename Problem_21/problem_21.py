#!/usr/bin/python


import time
from utils.utils import print_time_log


def sum_of_proper_divisors(number: int):
    '''
    Let d(n) be defined as the sum of proper divisors of n
    (numbers less than n which divide evenly into n).
    :param number:
    :return:
    '''
    divisors = []

    for n in range(1, number):
        if number % n == 0:
            divisors.append(n)

    return sum(divisors)


def sum_of_amicable_numbers(number: int):
    '''
    Evaluate the sum of all the amicable numbers under -> number
    :param number:
    :return:
    '''
    start_time = time.time()
    amicable = set()

    for n in range(1, number):
        if n not in amicable:
            a = sum_of_proper_divisors(n)
            b = sum_of_proper_divisors(a)
            if (n == b) and not (n == b == a):
                # print('n: {0}, a: {1}, b: {2}'.format(n, a, b)) #  debug only
                amicable.add(n)
                amicable.add(a)

    result = sum(amicable)
    # print('amicable: {0}, result: {1}'.format(amicable, result)) #  debug only
    print_time_log(time.time() - start_time, result)
    return result
