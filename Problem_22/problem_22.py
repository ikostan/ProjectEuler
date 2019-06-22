#!/usr/bin/python


import time
import string
from utils.utils import print_time_log
from utils.utils import get_full_path


def file_reader():

    '''
    Use readline to read txt file python3:
    Source: https://stackoverflow.com/questions/28936140/use-readline-to-read-txt-file-python3
    How to get the current working directory using python3:
    https://stackoverflow.com/questions/17359698/how-to-get-the-current-working-directory-using-python-3
    :return:
    '''

    result = []
    '''
    file_path = ''
    if platform.system() == 'Linux':
        file_path = os.getcwd() + '/Problem_22/tests/p022_names.txt'  # linux
    elif platform.system() == 'Windows':
        file_path = os.getcwd() + '\\p022_names.txt' # windows
    # elif platform.system() == 'Darwin':
        # file_path = os.getcwd() + '/Problem_22/tests/p022_names.txt'  # MacOS
    '''
    file_path = get_full_path('/Problem_22/tests', 'p022_names.txt')

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
