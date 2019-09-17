#!/usr/bin/python

import time
from utils.utils import print_time_log


def is_pandigital(multiplicand: int, multiplier: int, pattern: str):
    """
    We shall say that an n-digit number is pandigital
    if it makes use of all the digits 1 to n exactly once;
    for example, the 5-digit number, 15234, is 1 through 5 pandigital.

    :param multiplicand:
    :param multiplier:
    :param pattern:
    :return:
    """

    product = multiplicand * multiplier
    numbers = [multiplicand, multiplier, product]
    result = ''.join(sorted([char
                             for char in ''.join([str(n)
                                                  for n in numbers])], reverse=True))

    return result == pattern


def sum_of_all_products(limit: int):
    """
    Find the sum of all products whose multiplicand/multiplier/product
    identity can be written as a 1 through 9 pandigital.

    :param limit:
    :return:
    """

    start_time = time.time()
    pattern = str(limit)
    products = set()

    for a in range(1, 99, 1):

        for b in range(9999, 100, -1):

            if is_pandigital(a, b, pattern):
                products.add(a * b)

    result = sum(products)
    print_time_log(start_time, result)
    return result
