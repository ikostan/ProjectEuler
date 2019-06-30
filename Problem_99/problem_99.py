#!/usr/bin/python


from utils.utils import *
import time


def file_reader():

    result = []

    folder_name = '/Problem_99/tests'
    file_name = 'p099_base_exp.txt'
    file_path = get_full_path(folder_name, file_name)

    with open(file_path) as source:
        for line in source:
            temp = [int(t) for t in line.split(',')]
            result.append(temp)

    return result


def get_max_number():

    data = file_reader()

    start_time = time.time()
    max_number = 0
    line_number = 0

    for i, pair in enumerate(data):

        if len(str(pair[0])) > 5 and len(str(pair[1])) > 5:
            number = pair[0] ** pair[1]
            if number > max_number:
                max_number = number
                line_number = i

    print_time_log(start_time, line_number)
    return max_number
