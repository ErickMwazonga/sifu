'''
983. Minimum Cost For Tickets
Link: https://leetcode.com/problems/minimum-cost-for-tickets/
Resource: https://www.youtube.com/watch?v=4pY1bsBpIY4&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=3

You have planned some train traveling one year in advance.
The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:
a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.

Example 1:
Input: days = [1, 4, 6, 7, 8, 20], costs = [2, 7, 15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.
'''


class Solution:
    _MAX = float('inf')

    def mincostTickets(self, days: list[int], costs: list[int]) -> int | float:
        costs = list(zip([1, 7, 30], costs))
        return self.backtrack(days, costs, 0, {}, 0)

    def backtrack(self, days, costs, i, memo, upto_day)  -> int | float:
        if i >= len(days):
            return 0

        if (i, upto_day) in memo:
            return memo[(i, upto_day)]

        min_cost = self._MAX
        for choice, cost in costs:
            j = i
            while j < len(days) and days[j] < days[i] + choice:
                j += 1

            min_cost = min(
                min_cost,
                cost + self.backtrack(days, costs, j, memo, days[j - 1])
            )

        memo[(i, upto_day)] = min_cost
        return min_cost
