#!/usr/bin/python


from Problems_1_to_100.Problem_19.calendar import Calendar


class Date:

    def __init__(self, day: int, week: str, month: str, year: int):
        self.date = dict()
        self.date['month'] = self.__set_month__(month)
        self.date['day'] = self.__set_day__(day, month, year)
        self.date['week'] = self.__set_week__(week)
        self.date['year'] = self.__set_year__(year)

    @classmethod
    def __set_day__(cls, day: int, month: str, year: int):

        is_leap = Calendar.is_leap(year)

        if is_leap and month == Calendar.month_name[1]:
            # February as leap year:
            if day < 1 or day > 29:
                raise ValueError(
                    "Invalid Day (leap year): {0}. Total days {1} in month {2}".format(
                        day, Calendar.months[month], month))
        else:
            if day < 1 or day > Calendar.months[month]:
                raise ValueError(
                    "Invalid Day: {0}. Total days {1} in month {2}".format(
                        day, Calendar.months[month], month))

        return day

    @classmethod
    def __set_week__(cls, week: str):
        if week == '':
            return Calendar.week_days[0]
        elif week not in Calendar.week_days:
            raise ValueError(
                "Invalid Week Day: {0}.".format(week))
        return week

    @classmethod
    def __set_month__(cls, month: str):
        if month not in Calendar.months.keys():
            raise ValueError(
                "Invalid Month: {0}.".format(month))
        return month

    @classmethod
    def __set_year__(cls, year: int):
        if year < 1900 or year > 2999:
            raise ValueError(
                "Invalid Year: {0}. Valid year must be between 1900 and 2000".format(year))
        return year

    def get_day(self):
        return self.date['day']

    def set_day(self, day: int):

        try:
            self.date['day'] = self.__set_day__(day, self.get_month(), self.get_year())
            self.__update_week__()
        except ValueError as err:
            # print(err.args)
            self.date['day'] = 1
            self.__update_week__()
            self.__update_month__()
            raise

    def get_week(self):
        return self.date['week']

    def get_month(self):
        return self.date['month']

    def __update_week__(self):
        week_index = Calendar.week_days.index(self.date['week'])

        if week_index < len(Calendar.week_days) - 1:
            self.date['week'] = Calendar.week_days[week_index + 1]
        else:
            self.date['week'] = Calendar.week_days[0]

    def __update_month__(self):
        index = Calendar.month_name.index(self.get_month()) + 1
        # print('__update_month__: index ->{0}, len: {1}'.format(index, len(Calendar.month_name) - 1))

        if index <= len(Calendar.month_name) - 1:
            self.date['month'] = Calendar.month_name[index]
        else:
            self.date['year'] = self.__set_year__(self.date['year'] + 1)
            self.date['month'] = self.__set_month__(Calendar.month_name[0])

    def get_year(self):
        return self.date['year']
