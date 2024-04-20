'''
122. Best Time to Buy and Sell Stock II
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Resource: https://medium.com/@rebeccahezhang/leetcode-122-best-time-to-buy-and-sell-stock-ii-fbf6d66d62e3
Resource: https://www.youtube.com/watch?v=3SJ3pUkPQMc

Say you have an array prices for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit.
You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time 
(i.e., you must sell the stock before you buy again).

Example:
Input: [7, 1, 5, 3, 6, 4] -> 7
Explanation: 
    Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
    Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return self.calculate(prices, 0, False, {})

    def calculate(self, prices: list[int], idx: int, has_share: bool, memo: dict) -> int:
        if idx == len(prices):
            return 0

        if (idx, has_share) in memo:
            return memo[(idx, has_share)]

        if has_share:
            # skip day
            skip = self.calculate(prices, idx + 1, has_share, memo)
            # sell and move on to the next day
            sell = self.calculate(prices, idx + 1, False, memo) + prices[idx]
            # sell and buy the same day
            buy_sell = self.calculate(prices, idx + 1, True, memo)
            res = max(skip, sell, buy_sell)
        else:
            # skip day
            skip = self.calculate(prices, idx + 1, has_share, memo)
            # buy share and move on
            buy = self.calculate(prices, idx + 1, True, memo) - prices[idx]
            res = max(skip, buy)

        memo[(idx, has_share)] = res
        return res


soln = Solution()

assert soln.max_profit([7, 1, 5, 3, 6, 4]) == 7
assert soln.max_profit([1, 2, 3, 4, 5]) == 4
assert soln.max_profit([7, 6, 4, 3, 1]) == 0
