#!/usr/bin/python


import time
from utils.utils import print_time_log


def find_greatest_product(number: str, adjacent_digits: int):
    start_time = time.time()
    result = 0
    start = 0
    end = adjacent_digits

    while end < len(number):
        subset = [int(i) for i in number[start:end]]
        temp = multiply_members(subset)
        if result < temp:
            result = temp
        start += 1
        end += 1

    print_time_log(start_time, result)
    return result


def multiply_members(digits: list):
    n = 1

    if 0 in digits:
        return 0

    for i in digits:
        n *= i

    return n
