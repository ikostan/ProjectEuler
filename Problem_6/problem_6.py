#!/usr/bin/python


import time
import math


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


# This function is used for logging processing time only
# Shows how long it took in order to get the answer
def print_time_log(end_time: time, result=''):
    if end_time < 60:
        print("The answer {0} returned in {1} seconds".format(
            result, end_time))
    else:
        minutes = int(end_time / 60)
        seconds = end_time - (minutes * 60)
        print("The answer {0} returned in {1} minutes and {2} seconds".format(
            result, minutes, seconds))
