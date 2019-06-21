#!/usr/bin/python


import time
import math
from Template.problem_ import print_time_log


def find_triplet(num: int):
    start_time = time.time()
    a, b = 1, 1

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
                    print_time_log(end_time, result)
                    return result
            b += 1
        a += 1
