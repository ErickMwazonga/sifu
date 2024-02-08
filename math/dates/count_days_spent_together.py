'''
2409. Count Days Spent Together
https://leetcode.com/problems/count-days-spent-together/

Alice and Bob are traveling to Rome for separate business meetings.
You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. 
Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), 
while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). 
Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.

Return the total number of days that Alice and Bob are in Rome together.
You can assume that all dates occur in the same calendar year, which is not a leap year. 
Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].

Example 1:
Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
Output: 3
Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.

Example 2:
Input: arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
Output: 0
Explanation: There is no day when Alice and Bob are in Rome together, so we return 0.
'''

class CustomDate:

    def __init__(self, date: str) -> None:
        month, day = date.split('-')
        self.month = int(month)
        self.day = int(day)

    def __eq__(self, other: 'CustomDate') -> bool:
        return self.month == other.month and self.day == other.day

    def __gt__(self, other: 'CustomDate') -> bool:
        if self.month > other.month:
            return True
        if self.month == other.month:
            return self.day > other.day
        
        return False
    
    def __lt__(self, other: 'CustomDate') -> bool:
        return not self > other and not self == other 

    def __le__(self, other: 'CustomDate') -> bool:
        return self < other or self == other

    def __ge__(self, other: 'CustomDate') -> bool:
        return self > other or self == other

    def __sub__(self, other: 'CustomDate') -> int:
        if self.month == other.month:
            return abs(self.day - other.day)
        
        start_date = min(self, other) # self if self.month < other.month else other
        end_date = max(self, other) # self if self.month > other.month else other

        # add remaining days of the start month
        total_days = self.no_of_days_in_month(start_date.month) - start_date.day

        # add days into the end month
        total_days += end_date.day

        for month in range(start_date.month + 1, end_date.month):
            total_days += self.no_of_days_in_month(month)

        return total_days
    
    def no_of_days_in_month(self, month: int) -> int:
        mapping = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return mapping[month - 1]
    

class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        arriveAlice, leaveAlice = CustomDate(arriveAlice), CustomDate(leaveAlice)
        arriveBob, leaveBob = CustomDate(arriveBob), CustomDate(leaveBob)

        if leaveAlice < arriveBob or leaveBob < arriveAlice:
            return 0
        
        arrival = max(arriveAlice, arriveBob)
        departure = min(leaveAlice, leaveBob)

        return departure - arrival + 1
