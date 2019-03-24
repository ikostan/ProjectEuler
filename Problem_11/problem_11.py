#!/usr/bin/python


import time


def get_max_product(numbers: list, counter: int):
    start_time = time.time()
    result = 0
    end_time = time.time() - start_time

    temp = process_diagonal(numbers, counter)
    if result < temp:
        result = temp

    temp = process_columns(numbers, counter)
    if result < temp:
        result = temp

    temp = process_rows(numbers, counter)
    if result < temp:
        result = temp

    print_log(end_time, result)
    return result


def process_diagonal(numbers: list, counter: int):
    result = 0
    row, col = 0, 0

    while row + (counter - 1) <= (len(numbers) - 1) and col + (counter - 1) <= (len(numbers[0]) - 1):
        tem_arr = [numbers[row][col], numbers[row + 1][col + 1], numbers[row + 2][col + 2], numbers[row + 3][col + 3]]
        temp = multiply_members(tem_arr)
        if temp > result:
            result = temp
        row += 1
        col += 1

    row, col = 0, (len(numbers[0]) - 1)
    while row + (counter - 1) <= (len(numbers) - 1) and col >= (counter - 1):
        tem_arr = [numbers[row][col], numbers[row + 1][col - 1], numbers[row + 2][col - 2], numbers[row + 3][col - 3]]
        temp = multiply_members(tem_arr)
        if temp > result:
            result = temp
        row += 1
        col -= 1

    return result


def process_columns(numbers: list, counter: int):
    result = 0

    col = 0
    while col < len(numbers[0]):
        row = 0
        while row < (len(numbers) - counter):
            temp_arr = [numbers[row][col], numbers[row + 1][col], numbers[row + 2][col], numbers[row + 3][col]]
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


def multiply_members(numbers: list):
    result = 1

    if 0 in numbers:
        return 0

    for i in numbers:
        result *= i

    return result


def print_log(end_time, result):
    if end_time < 60:
        print("The answer {0} returned in {1} seconds".format(result, end_time))
    else:
        minutes = int(end_time / 60)
        seconds = end_time - (minutes * 60)
        print("The answer {0} returned in {1} minutes and {2} seconds".format(result, minutes, seconds))