#!/usr/bin/python


import time


def triangle_number_generator(limit: int):
    triangle = {'counter': 0, 'total': 0, 'number': 1}
    while triangle['number'] <= limit:
        triangle['total'] += triangle['number']
        triangle['counter'] += 1
        triangle['number'] += 1
    # Debug only:
    print("counter:{0}, number:{1}".format(triangle['counter'], triangle['total']))
    return triangle


def print_time_log(end_time: time, result):
    if end_time < 60:
        print("The answer {0} returned/"
              " in {1} seconds".format(result, end_time))
    else:
        minutes = int(end_time / 60)
        seconds = end_time - (minutes * 60)
        print("The answer {0} returned/"
              " in {1} minutes and {2} seconds".format(result, minutes, seconds))

