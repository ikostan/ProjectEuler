#!/usr/bin/python


import time


def collatz_sequence(starting_number: int, is_first_run=True):

    if is_first_run:
        # Printing with no newlines in Python 3
        print(str(starting_number) + " -> ", end='')

    # Terminate execution
    if starting_number == 1:
        print(str(1), end='')
        return

    # Collatz sequence
    if starting_number % 2 == 0:
        starting_number = starting_number // 2
    else:
        starting_number = (starting_number * 3) + 1

    if starting_number != 1:
        # Printing with no newlines in Python 3
        print(str(starting_number) + " -> ", end='')

    collatz_sequence(starting_number, False)


# This function is used for logging processing time only
# Shows how long it took in order to get the answer
def print_time_log(end_time: time, result):
    if end_time < 60:
        print("The answer {0} returned in {1} seconds".format(
            result, end_time))
    else:
        minutes = int(end_time / 60)
        seconds = end_time - (minutes * 60)
        print("The answer {0} returned in {1} minutes and {2} seconds".format(
            result, minutes, seconds))

