#!/usr/bin/python


from utils.utils import print_time_log, is_pandigital
import time
import itertools


def has_sub_string_divisibility(number: list):
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

    if number[0] == 0:
        return False

    # d2d3d4=406 is divisible by 2
    temp = number[1] * 100 + number[2] * 10 + number[3]
    if temp % 2 == 0 and temp < 1000:

        # d3d4d5=063 is divisible by 3
        temp = number[2] * 100 + number[3] * 10 + number[4]
        if temp % 3 == 0 and temp < 1000:

            # d4d5d6=635 is divisible by 5
            temp = number[3] * 100 + number[4] * 10 + number[5]
            if temp % 5 == 0 and temp < 1000:

                # d5d6d7=357 is divisible by 7
                temp = number[4] * 100 + number[5] * 10 + number[6]
                if temp % 7 == 0 and temp < 1000:

                    # d6d7d8=572 is divisible by 11
                    temp = number[5] * 100 + number[6] * 10 + number[7]
                    if temp % 11 == 0 and temp < 1000:

                        # d7d8d9=728 is divisible by 13
                        temp = number[6] * 100 + number[7] * 10 + number[8]
                        if temp % 13 == 0 and temp < 1000:

                            # d8d9d10=289 is divisible by 17
                            temp = number[7] * 100 + number[8] * 10 + number[9]
                            if temp % 17 == 0 and temp < 1000:
                                return True
                            return False
                        return False
                    return False
                return False
            return False
        return False


def main():

    start_time = time.time()
    num_sets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    combinations = set()

    for combination in itertools.permutations(num_sets):
        if has_sub_string_divisibility(combination):
            combinations.add(int(''.join([str(c) for c in combination])))

    result = sum(combinations)
    print_time_log(start_time, result)
    return result
