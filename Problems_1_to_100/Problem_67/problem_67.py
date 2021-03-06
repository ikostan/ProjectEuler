#!/usr/bin/python

import time
from utils.utils import print_time_log
from utils.utils import get_full_path


def find_maximum_total(triangle: list):

    start_time = time.time()
    new_triangle = triangle

    for n in range(0, len(new_triangle) - 1):
        if len(new_triangle[n]) < 2:
            new_triangle[n + 1][0] += new_triangle[n][0]
            new_triangle[n + 1][1] += new_triangle[n][0]
        else:
            for i in range(0, len(new_triangle[n]) + 1):
                if i - 1 < 0:
                    new_triangle[n + 1][i] += new_triangle[n][i]
                elif i - 1 >= 0 and i < len(new_triangle[n]):
                    temp = max(new_triangle[n][i - 1],
                               new_triangle[n][i])
                    new_triangle[n + 1][i] += temp
                else:
                    new_triangle[n + 1][i] += new_triangle[n][i - 1]

    result = max(new_triangle[-1])
    print_time_log(start_time, result)
    return result


def file_reader():
    """
    Use readline to read txt file python3:
    Source: https://stackoverflow.com/questions/
    28936140/use-readline-to-read-txt-file-python3

    How to get the current working directory using python3:
    https://stackoverflow.com/questions/17359698/
    how-to-get-the-current-working-directory-using-python-3
    :return:
    """

    result = []
    file_path = get_full_path('/Problems_1_to_100/Problem_67/tests',
                              'p067_triangle.txt')

    with open(file_path) as source:
        for line in source:
            temp = [int(t) for t in line.split(' ')]
            # print(temp)  # debug only
            result.append(temp)

    return result
