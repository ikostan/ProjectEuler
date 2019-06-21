#!/usr/bin/python


import time
from utils.utils import print_time_log


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
