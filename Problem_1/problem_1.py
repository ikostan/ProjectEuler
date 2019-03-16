#!/usr/bin/python


import time


def get_multiplies_of_3_and_5(max_num, nums):
    start = time.time()
    result = 0
    i = 0

    while i < max_num:
        if div_by_nums(i, nums):
            result += i
        i += 1

    elapsed = time.time() - start
    print("result {0} returned in {1} seconds".format(result, elapsed))
    return result


def div_by_nums(i, nums):
    for n in nums:
        if i % n == 0:
            return True
    return False

