#!/usr/bin/python


import time
from utils.utils import print_time_log
from Problem_19.date import Date


def is_leap(year: int):
    if year % 4 == 0:
        if str(year)[2:] == '00':
            if year % 400 == 0:
                return True
            return False
        else:
            return True
    return False


def main():

    '''
    Start date: 1 Jan 1900 was a Monday.

    How many Sundays fell on the first of the month
    during the twentieth century
    (1 Jan 1901 to 31 Dec 2000)?
    :return:
    '''

    start_time = time.time()

    stop_date = Date(31, '', Date.get_months()[11], 2000)
    current_date = Date(1, Date.week_days[0], Date.get_months()[0], 1900)
    sundays = []

    while (current_date.get_year() <= stop_date.get_year()) and \
            (current_date.get_day() <= stop_date.get_day()) and \
            (stop_date.get_month() == current_date.get_month()):
        pass

    result = len(sundays)
    print_time_log(time.time() - start_time, result)

    return result
