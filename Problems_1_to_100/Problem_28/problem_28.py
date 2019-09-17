#!/usr/bin/python

import time
from utils.utils import print_time_log


direction = ['left', 'down', 'right', 'up']

position = {
        'row': 0,
        'col': 0,
        'counter': 0,
        'direction': '',
        'length_vertical': 0,
        'length_horizontal': 0
    }


def calc_total(data: list):
    """
    Returns sum of the numbers on the diagonals

    :param data:
    :return:
    """

    start_time = time.time()
    size = len(data)
    total = 0

    for a in range(0, size):
        b = size - 1 - a
        if b != a:
            total += data[a][a] + data[a][b]
        else:
            total += data[a][a]

    print_time_log(start_time, total)
    return total


def update_grid_line(data: list, size: int):
    """
    Updates data grid

    :param data:
    :param size:
    :return:
    """
    length = 0

    if position['direction'] == direction[0] or position['direction'] == direction[2]:
        length = position['length_horizontal']

    if position['direction'] == direction[1] or position['direction'] == direction[3]:
        length = position['length_vertical']

    for step in range(0, length):

        # MOVE LEFT:
        if position['direction'] == direction[0]:
            position['col'] = position['col'] + 1

        # MOVE RIGHT:
        if position['direction'] == direction[2]:
            position['col'] = position['col'] - 1

        # MOVE DOWN:
        if position['direction'] == direction[1]:
            position['row'] = position['row'] + 1

        # MOVE UP:
        if position['direction'] == direction[3]:
            position['row'] = position['row'] - 1

        position['counter'] += 1
        data[position['row']][position['col']] = position['counter']

    update_position(size)
    return data


def data_generator(size: int, debug=False):
    """
    Moves position object trough data grid until get to the final point.

    Starting with the number 1 and moving to the right in a clockwise direction
    a 5 by 5 spiral is formed as follows:

        21 22 23 24 25
        20  7  8  9 10
        19  6  1  2 11
        18  5  4  3 12
        17 16 15 14 13

    :param size:
    :return data:
    """

    # generate data grid with all values = 0
    data = empty_grid_generator(size)

    # max possible number in the grid:
    max_counter = size * size

    # calculate coordinates for the center:
    center = len(data) // 2

    # set value in centre = 1
    data[center][center] = 1

    # set current position:
    position['counter'] = data[center][center]
    position['length_vertical'] = 1
    position['length_horizontal'] = 1
    position['row'] = center
    position['col'] = center
    position['direction'] = direction[0]

    while position['counter'] != max_counter:
        data = update_grid_line(data, size)

        # debug only:
        if debug:
            print('row: {0}, col: {1}, counter: {2}, direction: {3}'.format(
                position['row'],
                position['col'],
                position['counter'],
                position['direction']
            ))
            print(data[position['row']])

    return data


def update_position(size: int):
    """
    Updates direction inside position object
    Updates length inside position object

    :param size:
    :return:
    """

    # update horizontal length:
    if position['direction'] == direction[0] or position['direction'] == direction[2]:
        if position['length_horizontal'] + 1 < size:
            position['length_horizontal'] += 1

    # update vertical length:
    if position['direction'] == direction[1] or position['direction'] == direction[3]:
        if position['length_vertical'] + 1 < size:
            position['length_vertical'] += 1

    current_index = direction.index(position['direction'])

    if current_index == len(direction) - 1:
        position['direction'] = direction[0]
    else:
        position['direction'] = direction[current_index + 1]


def empty_grid_generator(size: int):
    """
    Generate data grid with all values = 0

    :param size:
    :return data:
    """

    #  generate grid with all values = 0
    data = [([0] * size) for i in range(0, size)]

    return data
