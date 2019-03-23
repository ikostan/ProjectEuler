#!/usr/bin/python


import time


def square_diff(start, end):
    start_time = time.time()
    result = square_of_sums(start, end) - sum_squares_of_numbers(start, end)
    end_time = time.time() - start_time
    print_log(end_time, result)
    return result

def sum_squares_of_numbers(start, end):
    result = 0
    return result


def square_of_sums(start, end):
    result = 0
    return result


def print_log(end_time, result):
    if end_time < 60:
        print("The answer {0} returned in {1} seconds".format(result, end_time))
    else:
        minutes = int(end_time / 60)
        seconds = end_time - (minutes * 60)
        print("The answer {0} returned in {1} minutes and {2} seconds".format(result, minutes, seconds))