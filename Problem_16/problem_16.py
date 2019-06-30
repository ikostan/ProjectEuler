#!/usr/bin/python


import time
import math
from utils.utils import print_time_log


def find_the_sum(number: int, power: int):

    start_time = time.time()
    powered_number = int(math.pow(number, power))
    n_list = [int(i) for i in str(powered_number) if i != '0']
    result = sum(n_list)
    print_time_log(start_time, result)
    return result
