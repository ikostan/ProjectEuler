#!/usr/bin/python


from utils.utils import *
import time
import math


def file_reader():

    result = []

    folder_name = '/Problems_1_to_100/Problem_99/tests'
    file_name = 'p099_base_exp.txt'
    file_path = get_full_path(folder_name, file_name)

    line_num = 1
    with open(file_path) as source:
        for line in source:
            temp = [int(t) for t in line.split(',')]
            temp.append(line_num)
            result.append(temp)
            line_num += 1

    return result


def get_largest_result_line_num(data: list):
    '''
    The best approach is using logarithms.
    One of the rules of logarithms is the power rule which states:

    a^c > b^f ==> c * log(a) > f * log(b)

    Another way to compare a^x and b^y is to compare a and b^(y/x) instead.
    :param data:
    :return:
    '''

    start_time = time.time()
    max_line_num = 0
    max_log = 0

    for segment in data:
        log = segment[1] * math.log(segment[0])
        if log > max_log:
            max_log = log
            max_line_num = segment[-1]

    print_time_log(start_time, max_line_num)
    return max_line_num
