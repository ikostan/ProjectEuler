#!/usr/bin/python


def find_even_fibonacci(max_num):
    nums = generate_fibonacci(max_num)
    result = sum([i for i in nums if i % 2 == 0])
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

