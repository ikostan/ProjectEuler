#!/usr/bin/python


import time
import math


def find_the_sum(number: int, power: int):
    start_time = time.time()
    powered_number = int(math.pow(number, power))
    n_list = [int(i) for i in str(powered_number) if i != '0']
    result = sum(n_list)
    end_time = time.time() - start_time
    print_time_log(end_time, result)
    return result


# This function is used for logging processing time only
# Shows how long it took in order to get the answer
def print_time_log(end_time: time, result):
    if end_time < 60:
        print("The answer {0} returned in {1} seconds".format(
            result, end_time))
    else:
        minutes = int(end_time / 60)
        seconds = end_time - (minutes * 60)
        print("The answer {0} returned in {1} minutes and {2} seconds".format(
            result, minutes, seconds))
