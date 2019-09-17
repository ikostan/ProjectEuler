#!/usr/bin/python

from utils.utils import print_time_log, is_pentagonal, pentagonal_number_generator
import time


def main():

    start_time = time.time()
    generator = pentagonal_number_generator()
    pentagonals = set()
    pentagonals.add(next(generator))

    while True:

        b = next(generator)
        for a in pentagonals:
            if is_pentagonal(a + b) and is_pentagonal(abs(a - b)):
                print_time_log(start_time, abs(a - b))
                return abs(a - b)

        pentagonals.add(b)
