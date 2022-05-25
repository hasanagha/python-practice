''' method which returns a day of the number when date (yyyy-mm-dd) is passed 
    for example: 2020-01-01 should return 01
                 2022-02-09 should return 40
'''
import datetime


def dayOfYear(date):
    year_check = int(date[0:4])
    leap = 1 if (year_check % 400 == 0) or (year_check % 4 == 0 and year_check % 100 != 0) else 0

    day1 = datetime.datetime(int(date[0:4]), int(date[5:7]), int(date[8:10]))
    day2 = datetime.datetime(int(date[0:4]), int(12) , int(31))

    ans = 365 - (day2 - day1).days + leap

    return ans