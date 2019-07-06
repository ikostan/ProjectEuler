#!/usr/bin/python


from utils.utils import print_time_log, is_pandigital
import time
import itertools


def has_property(number: str):
    '''
    The number, 1406357289, is a 0 to 9 pandigital number.
    Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

        d2d3d4=406 is divisible by 2
        d3d4d5=063 is divisible by 3
        d4d5d6=635 is divisible by 5
        d5d6d7=357 is divisible by 7
        d6d7d8=572 is divisible by 11
        d7d8d9=728 is divisible by 13
        d8d9d10=289 is divisible by 17

    :param number:
    :return:
    '''

    number = str(number)
    size = len(number)

    # d2d3d4=406 is divisible by 2
    if int(number[1:4]) % 2 != 0:
        return False

    # d3d4d5=063 is divisible by 3
    if int(number[2:5]) % 3 != 0:
        return False

    # d4d5d6=635 is divisible by 5
    if int(number[3:6]) % 5 != 0:
        return False

    # d5d6d7=357 is divisible by 7
    if int(number[4:7]) % 7 != 0:
        return False

    # d6d7d8=572 is divisible by 11
    if int(number[5:8]) % 11 != 0:
        return False

    # d7d8d9=728 is divisible by 13
    if int(number[6:9]) % 13 != 0:
        return False

    # d8d9d10=289 is divisible by 17
    if int(number[7:10]) % 17 != 0:
        return False

    return True


def main():

    start_time = time.time()
    num_sets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    combinations = set()
    for permutation in itertools.permutations(num_sets):
        str_format = ''.join([str(p) for p in permutation])
        if str_format[0] != '0' and \
                is_pandigital(str_format) and \
                has_property(str_format):
            combinations.add(int(str_format))

    result = sum(combinations)
    print_time_log(start_time, result)
    return result
