#!/usr/bin/python


from utils.utils import print_time_log
import time


def is_contain_same_digits(a: int):
    numbers = []
    for n in range(2, 7):
        numbers.append(a * n)

    for n in numbers:
        if sorted([int(s) for s in str(numbers[0])]) != sorted([int(s) for s in str(n)]):
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
