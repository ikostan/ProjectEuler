#!/usr/bin/python


from utils.utils import print_time_log, is_palindrome
import time


def convert_to_binary(number: int):
    '''
    code for converting a decimal number to it’s binary equivalent
    :param number:
    :return:
    '''
    return bin(number).replace("0b","")


def calc_sum_of_palindromic_numbers(limit: int):

    start_time = time.time()
    palindromes = set()

    for n in range(1, limit):
        if is_palindrome(n) and is_palindrome(convert_to_binary(n)):
            palindromes.add(n)

    result = sum(palindromes)
    print_time_log(start_time, result)
    return result
