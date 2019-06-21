#!/usr/bin/python


import time


def smallest_multiple(start: int, end: int):
    start_time = time.time()
    tested = end
    is_done = False

    if start == 1:
        start += 1

    numbers = range(start, end + 1)

    while not is_done:
        is_done = True

        for i in numbers:
            if tested % i != 0:
                is_done = False
                break

        if not is_done:
            # because the number should be divisible by "end" at least
            tested += end

    end_time = time.time() - start_time
    print_time_log(end_time, tested)

    return tested


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
