#!/usr/bin/python


import time
from utils.utils import print_time_log
from Problem_19.date import Date
from Problem_19.calendar import Calendar


def main(stop_date: Date, current_date: Date):

    '''
    Start date: 1 Jan 1900 was a Monday.

    How many Sundays fell on the first of the month
    during the twentieth century
    (1 Jan 1901 to 31 Dec 2000)?
    :return:
    '''

    start_time = time.time()
    sundays = 0

    while current_date.get_year() <= stop_date.get_year():

        for day in range(2, 33, 1):
            '''
            print("{0}, {1}, {2}, {3}".format(current_date.get_day(),
                                              current_date.get_month(),
                                              current_date.get_year(),
                                              current_date.get_week()))
            '''
            try:
                if current_date.get_day() == 1 and \
                        current_date.get_week() == Calendar.week_days[6] and \
                        current_date.get_year() >= 1901:
                    sundays += 1
                    '''
                    print("\nSunday fell on the first of the month:")
                    print("{0}, {1}, {2}, {3}\n".format(current_date.get_day(),
                                                        current_date.get_month(),
                                                        current_date.get_year(),
                                                        current_date.get_week()))
                    '''

                # if current_date.get_day() == day:
                    # continue

                current_date.set_day(day)

            except ValueError:
                # print(err.args)
                break

    print_time_log(time.time() - start_time, sundays)

    return sundays
