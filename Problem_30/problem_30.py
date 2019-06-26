#!/usr/bin/python


from utils.utils import print_time_log
import time


def is_sum_of_powers_of_their_digits(digit: int, power: int):
    '''
    Verify is the number can be written as the sum of
    'power' powers of their digits
    :param digit:
    :param power:
    :return:
    '''
    return digit == eval(' + '.join(str((int(d) ** power)) for d in str(digit)))


def main(power: int, limit: int):
    '''
    Find the sum of all the numbers that can be written as
    the sum of 'power' powers of their digits.
    :param power:
    :param limit:
    :return:
    '''
    numbers = list()
    for digit in range(2, limit):
        if is_sum_of_powers_of_their_digits(digit, power):
            numbers.append(digit)

    return sum(numbers)
