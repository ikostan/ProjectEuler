#!/usr/bin/python

import time
import itertools
from utils.utils import print_time_log


def lexicographic_permutations(numbers: list, index: int):
    """
    What is the millionth lexicographic permutation of
    the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
    :param numbers:
    :param index:
    :return:
    """

    start_time = time.time()
    result = int(''.join([str(l)
                          for l in
                          [list(i) for i in
                           itertools.permutations(numbers)][index]]))
    print_time_log(start_time, result)
    return result
