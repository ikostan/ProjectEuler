#!/usr/bin/python


import time
import math
from Template.problem_ import print_time_log


def square_diff(start, end):
    start_time = time.time()
    result = int(square_of_sums(start, end) - sum_squares_of_numbers(start, end))
    end_time = time.time() - start_time
    print_time_log(end_time, result)
    return result


def sum_squares_of_numbers(start, end):
    result = 0

    for i in range(start, end + 1):
        result += math.pow(i, 2)

    return result


def square_of_sums(start, end):
    result = math.pow(sum(range(start, end + 1)), 2)
    return result
