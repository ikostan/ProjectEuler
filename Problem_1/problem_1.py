#!/usr/bin/python


import time


def get_multiplies_of_3_and_5(num):
    start = time.time()
    result = 0
    i = 3

    while i < num:
        if i % 3 == 0 or i % 5 == 0:
            result += i
        i += 1

    elapsed = time.time() - start
    print("result {0} returned in {1} seconds".format(result, elapsed))
    return result

