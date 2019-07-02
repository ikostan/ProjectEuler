#!/usr/bin/python


from utils.utils import print_time_log
import time


def main(max_number: int):

    start_time = time.time()
    results = list()

    for n in range(3, max_number + 1):
        if is_equal(n):
            results.append(n)

    result = sum(results)
    print_time_log(start_time, result)
    return result


def sum_of_factorials(number: int):
    '''
    Find the sum of all numbers of the factorial of their digits.
    :param number:
    :return:
    '''

    numbers = [int(n) for n in str(number)]
    results = []

    for number in numbers:
        result = 1
        for n in range(1, number + 1):
            result *= n

        results.append(result)

    return sum(results)


def is_equal(number: int):
    '''
    Find if the sum of all numbers
    is equal to the sum of the factorial of their digits.
    :param number:
    :return:
    '''

    return number == sum_of_factorials(number)
