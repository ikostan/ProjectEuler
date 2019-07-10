#!/usr/bin/python


from utils.utils import print_time_log
import time


def is_contain_same_digits(a: int):

    sorted_test_sample = sorted(str(a * 2))

    for n in range(3, 7):
        if sorted_test_sample != sorted(str(a * n)):
            return False

    return True


def main(number: int):
    '''
    It can be seen that the number, 125874, and its double, 251748,
    contain exactly the same digits, but in a different order.

    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
    contain the same digits.
    :param number:
    :return:
    '''

    start_time = time.time()
    while True:
        if is_contain_same_digits(number):
            print_time_log(start_time, number)
            return number
        number += 1
