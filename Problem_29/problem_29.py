#!/usr/bin/python


from utils.utils import print_time_log
import time


def generate_terms(start: int, end: int):

    terms = set()

    for n in range(start, end + 1):
        for power in range(start, end + 1):
            terms.add(n ** power)

    return terms
