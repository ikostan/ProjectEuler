#!/usr/bin/python


import time
from utils.utils import print_time_log


def get_multiplies_of_3_and_5(max_num, nums):
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
    for n in nums:
        if i % n == 0:
            return True
    return False

