#!/usr/bin/python


import time
import math


def find_triplet(num: int):
    start_time = time.time()
    a, b = 1, 1
    result = 0

    while a < (num - 2):
        b = a + 1
        while b < (num - 3):
            c = num - (a + b)

            if c < b:
                break

            if a < b < c:
                if math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2):
                    print("a:{0}, b:{1}, c:{2}".format(a, b, c))
                    result = a*b*c
                    end_time = time.time() - start_time
                    print_log(end_time, result)
                    return result
            b += 1
        a += 1




def print_log(end_time, result):
    if end_time < 60:
        print("The answer {0} returned in {1} seconds".format(result, end_time))
    else:
        minutes = int(end_time / 60)
        seconds = end_time - (minutes * 60)
        print("The answer {0} returned in {1} minutes and {2} seconds".format(result, minutes, seconds))

