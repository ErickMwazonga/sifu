'''
123. Best Time to Buy and Sell Stock III
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
Resource: https://www.programcreek.com/2014/02/leetcode-best-time-to-buy-and-sell-stock-iii-java/

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note: You may not engage in multiple transactions at the same time
(i.e., you must sell the stock before you buy again).

Example:
Input: prices = [3, 3, 5, 0, 0, 3, 1, 4] -> 6
Explanation: 
    Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
    Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
'''



class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return self.solve(prices, 0, 2, False, {})

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
assert soln.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6
