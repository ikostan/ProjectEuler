#!/usr/bin/python

import time


def find_even_fibonacci(max_num):
    start_time = time.time()
    nums = generate_fibonacci(max_num)
    result = sum([i for i in nums if i % 2 == 0])
    print("result {0} returned in {1} seconds".format(result, time.time() - start_time))
    return result


def generate_fibonacci(max_num):
    nums = [1, 2]
    i = 0
    start = 0

    while i <= max_num:
        i = nums[start] + nums[start + 1]
        nums.append(i)
        start += 1

    return nums

