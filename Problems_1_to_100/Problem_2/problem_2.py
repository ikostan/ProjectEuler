#!/usr/bin/python

import time
from utils.utils import print_time_log


def find_even_fibonacci(max_num):

    start_time = time.time()
    nums = generate_fibonacci(max_num)
    result = sum([i for i in nums if i % 2 == 0])
    print_time_log(start_time, result)
    return result


# TODO: move this method into utils library
def generate_fibonacci(max_num):

    nums = [1, 2]
    i = 0
    start = 0

    while i <= max_num:
        i = nums[start] + nums[start + 1]
        nums.append(i)
        start += 1

    return nums
