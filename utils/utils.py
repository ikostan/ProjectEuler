#!/usr/bin/python


import time
import platform
import os


# This function is used for logging processing time only
# Shows how long it took in order to get the answer
def print_time_log(end_time: time, result=''):
    if end_time < 60:
        print("The answer {0} returned in {1} seconds".format(
            result, end_time))
    else:
        minutes = int(end_time / 60)
        seconds = end_time - (minutes * 60)
        print("The answer {0} returned in {1} minutes and {2} seconds".format(
            result, minutes, seconds))


# Returns full path based on differences between Linux and Windows
def get_full_path(file_folder: str, file_name: str, target_os=''):
    file_path = ''

    if target_os == '':
        target_os = platform.system()

    if target_os == 'Linux':
        file_path = os.getcwd() + '/' + file_folder + file_path  # linux
    elif target_os == 'Windows':
        file_path = os.getcwd() + '\\' + file_name  # windows
    # elif target_os == 'Darwin':
        # file_path = os.getcwd() + '/Problem_19/tests/leap_years.txt'  # MacOS
    return file_path
