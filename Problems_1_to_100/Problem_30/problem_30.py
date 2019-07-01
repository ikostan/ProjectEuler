#!/usr/bin/python


from utils.utils import print_time_log
import time


def calc_limit(power: int):
    '''
    One thing that is worth mentioning is that we should only
    check numbers less than 295245 (5∗9^5).
    This is the maximum number we can compose out of nines that
    has its sum of digits in fifth power ∑d^5 less than the actual number.
    Adding any single digit will go above that limit.
    :param power:
    :return:
    '''
    return (power + 1) * (9 ** power)


def is_sum_of_powers_of_their_digits(digit: int, power: int):
    '''
    Verify is the number can be written as the sum of
    'power' powers of their digits
    :param digit:
    :param power:
    :return:
    '''
    return digit == eval(' + '.join(str((int(d) ** power)) for d in str(digit)))


def main(power: int):
    '''
    Find the sum of all the numbers that can be written as
    the sum of 'power' powers of their digits.
    :param power:
    :param limit:
    :return:
    '''
    start_time = time.time()
    limit = calc_limit(power)
    result = 0

    for digit in range(2, limit):
        if is_sum_of_powers_of_their_digits(digit, power):
            result += digit

    print_time_log(start_time, result)
    return result
