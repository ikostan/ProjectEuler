#!/usr/bin/python
"""
Problem 1: Multiples of 3 and 5
Source: https://github.com/ikostan/ProjectEuler/tree/master/Problem_1
"""


import time
from utils.utils import print_time_log


def get_multiplies_of_3_and_5(max_num, nums):
    """
    Returns all multiplies of 3 and 5 within specified range
    :param max_num:
    :param nums:
    :return:
    """
    start_time = time.time()
    result = 0
    i = 0

    while i < max_num:
        if div_by_nums(i, nums):
            result += i
        i += 1

    print_time_log(start_time, result)
    return result


def div_by_nums(i, nums):
    """
    Test if number (i) is divisible by array of numbers (nums)
    :param i:
    :param nums:
    :return:
    """
    for n in nums:
        if i % n == 0:
            return True
    return False
