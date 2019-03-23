#!/usr/bin/python


import time


def find_greatest_product(number: str, adjacent_digits: int):
    start_time = time.time()
    result = 0
    start = 0
    end = adjacent_digits

    while end < len(number):
        subset = [int(i) for i in number[start:end]]
        temp = multiply_members(subset)
        if result < temp:
            result = temp
        start += 1
        end += 1

    end_time = time.time() - start_time
    print_log(end_time, result)
    return result


def multiply_members(digits: list):
    n = 1

    if 0 in digits:
        return 0

    for i in digits:
        n *= i

    return n


def print_log(end_time, result):
    if end_time < 60:
        print("The answer {0} returned in {1} seconds".format(result, end_time))
    else:
        minutes = int(end_time / 60)
        seconds = end_time - (minutes * 60)
        print("The answer {0} returned in {1} minutes and {2} seconds".format(result, minutes, seconds))