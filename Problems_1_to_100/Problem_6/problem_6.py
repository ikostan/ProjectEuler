#!/usr/bin/python


import time
import math
from utils.utils import print_time_log


def square_diff(start, end):

    start_time = time.time()
    result = int(square_of_sums(start, end) - sum_squares_of_numbers(start, end))
    print_time_log(start_time, result)
    return result


def sum_squares_of_numbers(start, end):
    result = 0

    for i in range(start, end + 1):
        result += math.pow(i, 2)

    return result


def square_of_sums(start, end):
    result = math.pow(sum(range(start, end + 1)), 2)
    return result
