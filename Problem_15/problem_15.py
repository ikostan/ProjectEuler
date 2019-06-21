#!/usr/bin/python


import time
from utils.utils import print_time_log


def calc_lattice_path(width: int, height: int):
    start_time = time.time()
    head = multiply_members(list(range(max(width, height) + 1, width + height + 1)))

    if width == height:
        tail = multiply_members(list(range(1, max(width, height) + 1)))
    else:
        tail = multiply_members(list(range(1, min(width, height) + 1)))

    result = head / tail
    end_time = time.time() - start_time
    print_time_log(end_time, result)
    return result


def multiply_members(numbers: list):
    print(numbers)
    result = 1
    for n in numbers:
        result *= n

    return result
