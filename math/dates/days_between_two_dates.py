'''
1360. Number of Days Between Two Dates
https://leetcode.com/problems/number-of-days-between-two-dates/description/

Write a program to count the number of days between two dates.
The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

Example 1:
Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1

Example 2:
Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15

Constraints:
The given dates are valid dates between the years 1971 and 2100.
'''

import calendar
from datetime import datetime

class Solution:

    SECONDS_IN_A_DAY = 24 * 60 * 60

    def daysBetweenDates(self, date1: str, date2: str) -> int:
        a: list[int] = map(int, date1.split("-"))
        b: list[int] = map(int, date2.split("-"))

        a: float = datetime(*a).timestamp()
        b: float = datetime(*b).timestamp()

        return int(abs(a - b) / self.SECONDS_IN_A_DAY)
    
class Solution_V2:

    def daysBetweenDates_v2(self, date1: str, date2: str) -> int:
        return abs(self.days_in_date(date1) - self.days_in_date(date2))

    def is_leap(self, year: int) -> bool:
        # return calendar.isleap(year)
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def days_in_year(self, year: int) -> int:
        return 366 if self.is_leap(year) else 365

    def days_in_month(self, year: int, month: int) -> int:
        if month == 2:
            return 29 if self.is_leap(year) else 28

        if month in {4, 6, 9, 11}:
            return 30
        
        return 31

    def days_in_date(self, date: str) -> int:
        year, month, days = map(int, date.split("-"))
        total: int = 0

        for year in range(1971, year):
            total += self.days_in_year(year)
        
        for month in range(1, month):
            total += self.days_in_month(year, month)

        total += days
        return total


        
                
        