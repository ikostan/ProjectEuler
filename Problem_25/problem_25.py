#!/usr/bin/python


import time
from utils.utils import print_time_log


def find_term(number: list, counter: int, length: int):
    '''
    Find the index of the first term in the Fibonacci sequence to contain 'length' digits
    :param number:
    :param counter:
    :param length:
    :return:
    '''

    start_time = time.time()
    while len(str(number[1])) < length:
        temp = number[1]
        number[1] += number[0]
        number[0] = temp
        counter += 1

    print_time_log(time.time() - start_time, counter)
    return counter
