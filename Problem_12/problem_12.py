#!/usr/bin/python


import time
import math
from Template.problem_ import print_time_log


def triangle_number_generator(limit: int):
    start_time = time.time()
    triangle = {'number': 1, 'dividers': 1, 'triangle': 1}
    while triangle['dividers'] <= limit:
        triangle['number'] += 1
        triangle['triangle'] += triangle['number']
        triangle = find_possible_dividers(triangle)
    end_time = time.time() - start_time
    print_time_log(end_time, triangle)
    return triangle


def find_possible_dividers(triangle: dict):
    # Reset dividers counter
    triangle['dividers'] = 0

    for n in range(1, int(math.sqrt(triangle['triangle'])) + 1):
        if triangle['triangle'] % n == 0:
            # If divisors are equal,
            # count only one
            if triangle['triangle'] / n == n:
                triangle['dividers'] += 1
            else:  # Otherwise count both
                triangle['dividers'] += 2
        n -= 1
    return triangle
