#!/usr/bin/python


import time
from Template.problem_ import print_time_log


def get_first_ten_digit(numbers: list, limit: int):
    start_time = time.time()
    string_number = str(sum(numbers))
    result = int(string_number[:limit])
    end_time = time.time() - start_time
    print_time_log(end_time, result)
    return result
