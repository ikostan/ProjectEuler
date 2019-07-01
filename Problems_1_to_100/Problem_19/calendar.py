#!/usr/bin/python


class Calendar:

    @classmethod
    def is_leap(cls, year: int):
        if year % 4 == 0:
            if str(year)[2:] == '00':
                if year % 400 == 0:
                    return True
                return False
            else:
                return True
        return False

    month_name = ['January', 'February', 'March', 'April',
                  'May', 'June', 'July', 'August',
                  'September', 'October', 'November', 'December']

    months = {'September': 30,
              'April': 30,
              'June': 30,
              'November': 30,
              'February': 28,
              'January': 31,
              'March': 31,
              'May': 31,
              'July': 31,
              'August': 31,
              'October': 31,
              'December': 31}

    week_days = ['Monday', 'Tuesday', 'Wednesday',
                 'Thursday', 'Friday', 'Saturday', 'Sunday']
