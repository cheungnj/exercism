from datetime import date
import calendar


class MeetupDayException(Exception):
    pass


def meetup_day(year, month, day_of_the_week, which):
    _, days_in_month = calendar.monthrange(year, month)
    if which == 'teenth':
        low = 13
        high = 20
    elif which == '1st':
        low = 1
        high = 8
    elif which == '2nd':
        low = 8
        high = 15
    elif which == '3rd':
        low = 15
        high = 22
    elif which == '4th':
        low = 22
        high = 29
    elif which == '5th':
        calendar.monthrange(year, month)
        low = 29
        high = days_in_month
    elif which == 'last':
        low = days_in_month - 6
        high = days_in_month + 1

    for i in range(low, high):
        if calendar.day_name[calendar.weekday(year, month, i)] == day_of_the_week:
            return date(year, month, i)

    msg = 'There is no {} {} of {} {}.'.format(which, day_of_the_week, calendar.month_name[month], year)
    raise MeetupDayException(msg)
