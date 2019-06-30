#!/usr/bin/python


import time
from utils.utils import print_time_log


def get_first_ten_digit(numbers: list, limit: int):

    start_time = time.time()
    string_number = str(sum(numbers))
    result = int(string_number[:limit])
    print_time_log(start_time, result)
    return result
