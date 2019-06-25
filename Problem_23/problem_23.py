#!/usr/bin/python


from utils.utils import print_time_log
import math
import time


# Function to calculate sum of divisors
def get_sum_short(n):
    sum_n = 0

    # Note that this loop runs till square root
    # of n
    i = 1
    while i <= (math.sqrt(n)):
        if n % i == 0:

            # If divisors are equal,take only one
            # of them
            if n / i == i:
                sum_n = sum_n + i
            else:  # Otherwise take both
                sum_n = sum_n + i
                sum_n = sum_n + (n / i)
        i = i + 1

    # calculate sum of all proper divisors only
    sum_n = sum_n - n
    return sum_n


# Function to check Abundant Number
def check_abundant(n):
    # Return true if sum of divisors is greater
    # than n.
    if get_sum_short(n) > n:
        return True
    else:
        return False


def get_sum_of_proper_divisors(n: int):
    '''
    proper divisor -> n % x == 0
    :param n:
    :return:
    '''

    return sum([x for x in range(1, n) if n % x == 0])


def define_number(n: int, sum_of_proper_divisors: int):
    '''
    A perfect number is a number for which the sum of its proper divisors
    is exactly equal to the number. For example, the sum of the proper
    divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
    which means that 28 is a perfect number.

    A number n is called deficient if the sum of its proper divisors is less than n.

    A number n is called abundant if the sum of its proper divisors exceeds n.
    :return:
    '''

    if n == sum_of_proper_divisors:
        return 'perfect'

    if n > sum_of_proper_divisors:
        return 'deficient'

    if n < sum_of_proper_divisors:
        return 'abundant'


def main(upper_limit: int):
    '''
    All integers greater than 28123 can be written as the sum of two abundant numbers.

    However, this upper limit cannot be reduced any further by analysis
    even though it is known that the greatest number
    that cannot be expressed as the sum of two abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written
    as the sum of two abundant numbers.
    :return:
    '''

    start_time = time.time()
    positive_integers = list(range(1, upper_limit + 1))
    all_abundant_numbers = set()

    for n in range(1, upper_limit + 1):
        if check_abundant(n):
            all_abundant_numbers.add(n)

    # print('all positive integers: {}'.format(len(positive_integers)))
    # print('abundant numbers in list: {}'.format(len(all_abundant_numbers)))

    abundant_numbers = sorted(list(all_abundant_numbers))
    all_abundant_numbers_rvs = sorted(all_abundant_numbers, reverse=True)
    # print('\nall_abundant_numbers_rvs {0}\n'.format(all_abundant_numbers_rvs))
    # print('\nall_abundant_numbers: {0}\n'.format(all_abundant_numbers))

    total = len(abundant_numbers)

    for a in all_abundant_numbers_rvs[0: total//2 + 1]:

        for b in abundant_numbers[0: total//2 + 1]:
            s = a + b

            if s > upper_limit:
                # print('BREAKING THE LOOP: {}'.format(s))
                break

            # if s in positive_integers:
                # positive_integers.remove(a + b)
            try:
                positive_integers.remove(a + b)
            except ValueError as err:
                #print('ERROR: {0} + {1} = {2} (not in list)'.format(a, b, s))
                pass
                # continue
        # print('LOOP -> positive integers left: {}'.format(len(positive_integers)))

    print('positive integers left: {}'.format(len(positive_integers)))
    result = sum(positive_integers)
    print_time_log(time.time() - start_time, result)

    return result
