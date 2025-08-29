'''
309. Best Time to Buy and Sell Stock with Cooldown
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
Resource: https://www.youtube.com/watch?v=I7j0F7AHpb8

You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example:
1. [1, 2, 3, 0, 2] -> 3 => transactions = [buy, sell, cooldown, buy, sell]
2. [1] -> 0
'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return self.solve(prices, 0, False, {})

    def solve(self, prices: list[int], idx: int, has_share: bool, memo: dict) -> int:
        if idx >= len(prices):
            return 0

        if (idx, has_share) in memo:
            return memo[(idx, has_share)]

        if has_share:
            # sell + cooldown
            sell = self.solve(prices, idx + 2, False, memo) + prices[idx]
            # skip
            skip = self.solve(prices, idx + 1, has_share, memo)
            res = max(sell, skip)
        else:
            # buy
            buy = self.solve(prices, idx + 1, True, memo) - prices[idx]
            # skip
            skip = self.solve(prices, idx + 1, has_share, memo)
            res = max(buy, skip)

        memo[(idx, has_share)] = res
        return res


soln = Solution()
assert soln.maxProfit([1, 2, 3, 0, 2]) == 3
assert soln.maxProfit([1]) == 0