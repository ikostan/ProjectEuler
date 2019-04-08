#!/usr/bin/python


import time


def find_maximum_total(triangle: list):
    start_time = time.time()
    numbers = list()
    i = 0
    for row in triangle:
        if len(row) > 1:
            if row[i] >= row[i + 1]:
                numbers.append(row[i])
            else:
                numbers.append(row[i + 1])
                i += 1
        else:
            numbers.append(row[i])
        print("{0}: {1}".format(i, row[i]))  # for debug purposes only

    print(numbers)  # for debug purposes only
    result = sum(numbers)
    end_time = time.time() - start_time
    print_time_log(end_time, result)

    #  For debug purposes only:
    if len(numbers) != len(triangle):
        print("ERROR: len of numbers: {0} does not equal to len of triangle: {1}".format(len(numbers), len(triangle)))

    return result


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
