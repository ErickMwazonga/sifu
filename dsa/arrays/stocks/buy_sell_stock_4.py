'''
188. Best Time to Buy and Sell Stock IV
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: k = 2, prices = [2, 4, 1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4 - 2 = 2

Example 2:
Input: k = 2, prices = [3, 2, 6, 5, 0, 3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6 - 2 = 4
Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3 - 0 = 3
'''

class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        return self.solve(prices, 0, k, False, {})

    def solve(self, prices: list[int], idx: int, k: int, has_share: bool, memo: dict) -> int:
        if idx == len(prices) or k == 0:
            return 0

        if (idx, k, has_share) in memo:
            return memo[(idx, k, has_share)]

        res = 0
        if has_share:
            # skip
            skip = self.solve(prices, idx + 1, k, has_share, memo)
            # sell
            sell = self.solve(prices, idx + 1, k - 1, False, memo) + prices[idx]
            res = max(skip, sell)
        else:
            # skip
            skip = self.solve(prices, idx + 1, k, has_share, memo)
            # buy
            buy = self.solve(prices, idx + 1, k, True, memo) - prices[idx]
            res = max(skip, buy)

        memo[(idx, k, has_share)] = res
        return res

soln = Solution()
assert soln.maxProfit(2, [2, 4, 1]) == 2
assert soln.maxProfit(2, [3, 2, 6, 5, 0, 3]) == 7