#!/usr/bin/python


import time
from utils.utils import print_time_log


def get_max_product(numbers: list, counter: int):

    start_time = time.time()
    result = 0

    temp = process_diagonal_down_left(numbers)
    if result < temp:
        result = temp

    temp = process_diagonal_down_right(numbers)
    if result < temp:
        result = temp

    temp = process_diagonal_up_left(numbers)
    if result < temp:
        result = temp

    temp = process_diagonal_up_right(numbers)
    if result < temp:
        result = temp

    temp = process_columns(numbers, counter)
    if result < temp:
        result = temp

    temp = process_rows(numbers, counter)
    if result < temp:
        result = temp

    print_time_log(start_time, result)
    return result


def process_diagonal_down_right(numbers: list):
    result = 0
    row = 0

    while row + 3 < len(numbers):
        col = 0
        while col + 3 < len(numbers[row]):
            temp_arr = [numbers[row][col], numbers[row + 1][col + 1],
                        numbers[row + 2][col + 2], numbers[row + 3][col + 3]]
            temp = multiply_members(temp_arr)
            if temp > result:
                result = temp
            col += 1
        row += 1
    return result


def process_diagonal_down_left(numbers: list):
    result = 0
    row = 0

    while row + 3 < len(numbers):
        col = len(numbers[row]) - 1
        while col - 3 >= 0:
            temp_arr = [numbers[row][col], numbers[row + 1][col - 1],
                        numbers[row + 2][col - 2], numbers[row + 3][col - 3]]
            temp = multiply_members(temp_arr)
            if temp > result:
                result = temp
            col -= 1
        row += 1
    return result


def process_diagonal_up_left(numbers: list):
    result = 0
    row = len(numbers) - 1

    while row - 3 >= 0:
        col = len(numbers[row]) - 1
        while col - 3 >= 0:
            temp_arr = [numbers[row][col], numbers[row - 1][col - 1],
                        numbers[row - 2][col - 2], numbers[row - 3][col - 3]]
            temp = multiply_members(temp_arr)
            if temp > result:
                result = temp
            col -= 1
        row -= 1
    return result


def process_diagonal_up_right(numbers: list):
    result = 0
    row = len(numbers) - 1

    while row - 3 >= 0:
        col = 0
        while col + 3 <= len(numbers[row]) - 1:
            temp_arr = [numbers[row][col], numbers[row - 1][col + 1],
                        numbers[row - 2][col + 2], numbers[row - 3][col + 3]]
            temp = multiply_members(temp_arr)
            if temp > result:
                result = temp
            col += 1
        row -= 1
    return result


def process_columns(numbers: list, counter: int):
    result = 0

    col = 0
    while col < len(numbers[0]):
        row = 0
        while row < (len(numbers) - counter):
            temp_arr = [numbers[row][col],
                        numbers[row + 1][col],
                        numbers[row + 2][col],
                        numbers[row + 3][col]]
            temp = multiply_members(temp_arr)
            if result < temp:
                result = temp
            row += 1
        col += 1

    return result


def process_rows(numbers: list, counter: int):
    result = 0

    for row in numbers:
        col = 0
        while col + (counter - 1) <= len(row):
            temp_arr = row[col:(col + counter)]
            temp = multiply_members(temp_arr)
            if result < temp:
                result = temp
            col += 1

    return result


# TODO: move this method into utils library
def multiply_members(numbers: list):
    result = 1

    if 0 in numbers:
        return 0

    for i in numbers:
        result *= i

    return result
