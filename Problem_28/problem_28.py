#!/usr/bin/python


from utils.utils import print_time_log
import time


def calc_sum(data:list):
    #center = len(data) // 2 + 1
    '''
    Returns sum of the numbers on the diagonals
    :param data:
    :return:
    '''
    size = len(data)
    sum = 0

    for a in range(0, size):
        b = size - 1 - a
        if b != a:
            sum += data[a][a] + data[a][b]
        else:
            sum += data[a][a]

    return sum


def data_generator(size: int):
    '''
    Starting with the number 1 and moving to the right in a clockwise direction
    a 5 by 5 spiral is formed as follows:

        21 22 23 24 25
        20  7  8  9 10
        19  6  1  2 11
        18  5  4  3 12
        17 16 15 14 13

    :param size:
    :return:
    '''
    data = list()
    return data
