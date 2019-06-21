#!/usr/bin/python


import time
from utils.utils import print_time_log


def calc_sum_of_digits(n: int):
    '''
    Calculates the sum of the digits in the number
    :param n:
    :return:
    '''

    start_time = time.time()
    factorial = calc_factorial(n)
    sum_of_digits = eval(' + '.join([i for i in str(factorial)]))

    end_time = time.time() - start_time
    print_time_log(end_time, sum_of_digits)

    return sum_of_digits


def calc_factorial(n: int):
    '''
    Calculate factorial for the number: n!
    :param n:
    :return:
    '''

    result = 1

    for num in range(1, n + 1):
        result *= num

    return result
