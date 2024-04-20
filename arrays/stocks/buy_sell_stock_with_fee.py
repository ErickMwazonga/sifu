'''
714. Best Time to Buy and Sell Stock with Transaction Fee
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/

You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, 
but you need to pay the transaction fee for each transaction.

Note:
You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.
 
Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Example 2:
Input: prices = [1, 3, 7, 5, 10, 3], fee = 3
Output: 6
'''

class Solution:
    def __init__(self) -> None:
        self.fee = None
        self.prices = None

    def maxProfit(self, prices: list[int], fee: int) -> int:
        self.fee = fee
        self.prices = prices

        return self.calculate(0, False, {})

    def calculate(self, idx: int, has_share: bool, memo: dict) -> int:
        if idx == len(self.prices):
            return 0

        if (idx, has_share) in memo:
            return memo[(idx, has_share)]

        if has_share:
            # skip day
            skip = self.calculate(idx + 1, has_share, memo)
            # sell, pay fee and move on
            sell = self.calculate(idx + 1, False, memo) + self.prices[idx] - self.fee
            res = max(skip, sell)
        else:
            # skip day
            skip = self.calculate(idx + 1, has_share, memo)
            # buy share and move on
            buy = self.calculate(idx + 1, True, memo) - self.prices[idx]
            res = max(skip, buy)

        memo[(idx, has_share)] = res
        return res


soln = Solution()
assert soln.maxProfit([1, 3, 2, 8, 4, 9], 2) == 8
assert soln.maxProfit([1, 3, 7, 5, 10, 3], 3) == 6
