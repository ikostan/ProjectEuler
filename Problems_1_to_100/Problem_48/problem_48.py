#!/usr/bin/python

from utils.utils import print_time_log
import time


def find_last_ten_digits(start: int, end: int):
    """
    Find the last ten digits of the series,
    11 + 22 + 33 + ... + 10001000.

    :param start:
    :param end:
    :return:
    """

    start_time = time.time()
    numbers = []

    for n in range(start, end + 1):
        numbers.append(n ** n)

    total = str(sum(numbers))
    result = total[- 10:]
    print_time_log(start_time, result)
    return result
