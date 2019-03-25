#!/usr/bin/python


import time
import math


def get_max_counter(starting_number: int):
    start_time = time.time()
    result = {'number': 1, 'counter': 1}

    while starting_number > 0:
        temp = get_collatz_counter(starting_number)
        if result['counter'] < temp:
            result['counter'] = temp
            result['number'] = starting_number
        starting_number -= 1

    end_time = time.time() - start_time
    print("number: {0} has {1} members chain".format(result['number'], result['counter']))
    print_time_log(end_time, result['number'])
    return result


def get_collatz_counter(starting_number: int):
    counter = 1
    n = starting_number

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1
        counter += 1

    return counter


def collatz_sequence(starting_number: int, is_first_run=True, counter=1):

    if is_first_run:
        # Printing with no newlines in Python 3
        print(str(starting_number) + " -> ", end='')

    # Terminate execution
    if starting_number == 1:
        print(str(1))
        print("Counter: {0}".format(counter))
        return

    # Collatz sequence
    if starting_number % 2 == 0:
        starting_number = starting_number // 2
    else:
        starting_number = (starting_number * 3) + 1

    if starting_number != 1:
        # Printing with no newlines in Python 3
        print(str(starting_number) + " -> ", end='')

    counter += 1
    collatz_sequence(starting_number, False, counter)


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

