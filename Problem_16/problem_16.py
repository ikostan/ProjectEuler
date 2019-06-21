#!/usr/bin/python


import time
import math
from Template.problem_ import print_time_log


def find_the_sum(number: int, power: int):
    start_time = time.time()
    powered_number = int(math.pow(number, power))
    n_list = [int(i) for i in str(powered_number) if i != '0']
    result = sum(n_list)
    end_time = time.time() - start_time
    print_time_log(end_time, result)
    return result
