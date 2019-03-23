#!/usr/bin/python


import time


def find_triplet(number:int):
    start_time = time.time()
    result = 0
    end_time = time.time() - start_time
    print_log(end_time, result)
    return result


def print_log(end_time, result):
    if end_time < 60:
        print("The answer {0} returned in {1} seconds".format(result, end_time))
    else:
        minutes = int(end_time / 60)
        seconds = end_time - (minutes * 60)
        print("The answer {0} returned in {1} minutes and {2} seconds".format(result, minutes, seconds))