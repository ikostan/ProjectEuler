#!/usr/bin/python


class Date:
    
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

    def __init__(self, day: int, week: str, month: str, year: int):

        self.date = dict()
        self.date['day'] = self.__set_day__(day, month)
        self.date['week'] = self.__set_week__(week)
        self.date['month'] = self.__set_month__(month)
        self.date['year'] = self.__set_year__(year)

    @classmethod
    def __set_day__(cls, day: int, month: str):
        if day < 1 or day > cls.months[month]:
            raise Exception(
                "Invalid Day: {0}. Total days {1} in month{2}".format(
                    day, cls.months[month], month))
        return day

    @classmethod
    def __set_week__(cls, week: str):
        if week == '':
            return cls.week_days[0]
        elif week not in cls.week_days:
            raise Exception(
                "Invalid Week Day: {0}.".format(week))
        return week

    @classmethod
    def __set_month__(cls, month: str):
        if month not in cls.months.keys():
            raise Exception(
                "Invalid Month: {0}.".format(month))
        return month

    @classmethod
    def __set_year__(cls, year: int):
        if year < 1900 or year > 2000:
            raise Exception(
                "Invalid Month: {0}. Valid year must be between 1900 and 2000".format(year))
        return year

    @classmethod
    def get_months(cls):
        return cls.month_name

    def get_day(self):
        return self.date['day']

    def get_week(self):
        return self.date['week']

    def get_month(self):
        return self.date['month']

    def get_year(self):
        return self.date['year']
