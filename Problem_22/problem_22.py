#!/usr/bin/python


import time
import platform
import os
import string


def file_reader():

    '''
    Use readline to read txt file python3:
    Source: https://stackoverflow.com/questions/28936140/use-readline-to-read-txt-file-python3
    How to get the current working directory using python3:
    https://stackoverflow.com/questions/17359698/how-to-get-the-current-working-directory-using-python-3
    :return:
    '''

    result = []
    file_path = ''
    if platform.system() == 'Linux':
        file_path = os.getcwd() + '/Problem_22/tests/p022_names.txt'  # linux
    elif platform.system() == 'Windows':
        file_path = os.getcwd() + '\\p022_names.txt' # windows
    # elif platform.system() == 'Darwin':
        # file_path = os.getcwd() + '/Problem_67/tests/p022_names.txt'  # MacOS

    with open(file_path) as source:
        for line in source:
            result = [t.replace('"', '') for t in line.split(',')]

    return sorted(result)


def alphabetical_value(name: str, alphabet: list):
    '''
    For example, when the list is sorted into alphabetical order,
    COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53
    :param name:
    :param alphabet:
    :return:
    '''

    result = 0
    for char in name:
        result += alphabet.index(char) + 1

    return result


def total_of_all_name_scores():
    '''
    Calculates the total of all the name scores in the file

    For example, when the list is sorted into alphabetical order,
    COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
    So, COLIN would obtain a score of 938 × 53 = 49714.

    :return:
    '''

    names = file_reader()
    alphabet = string.ascii_uppercase

    start_time = time.time()
    result = 0

    for i, name in enumerate(names):
        result += alphabetical_value(name, alphabet) * (i + 1)

    print_time_log(time.time() - start_time, result)
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
