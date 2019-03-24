#!/usr/bin/python


import time


def get_first_ten_digit(numbers: list, limit: int):
    start_time = time.time()
    string_number = str(sum(numbers))
    result = int(string_number[:limit])
    end_time = time.time() - start_time
    print_time_log(end_time, result)
    return result


def print_time_log(end_time: time, result):
    if end_time < 60:
        print("The answer {0} returned in {1} seconds".format(
            result, end_time))
    else:
        minutes = int(end_time / 60)
        seconds = end_time - (minutes * 60)
        print("The answer {0} returned in {1} minutes and {2} seconds".format(
            result, minutes, seconds))
