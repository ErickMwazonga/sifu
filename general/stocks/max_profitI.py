'''
https://medium.com/algorithms-and-leetcode/best-time-to-buy-sell-stocks-on-leetcode-the-ultimate-guide-ce420259b323
121. Best Time to Buy and Sell Stock
Say you have an array for which the ith element 
is the price of a given stock on day i.

If you were only permitted to complete at most one
transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
Example 1:
[7,1,5,3,6,4] -> 5
Explanation: 
Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

[7,6,4,3,1] -> 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''
from typing import List

# REVISIT - TODO
def maxProfit(prices: List[int]) -> int:
    '''Linear Time, Constant Space'''
    n = len(prices)
    if n < 2:
        return 0
    max_profit, min_stock = float('-inf'), prices[0]

    for p in prices:
        max_profit = max(max_profit, p - min_stock)
        min_stock = min(min_stock, p)

    return max_profit


assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert maxProfit([7, 6, 4, 3, 1]) == 0


# TODO
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if len (prices) < 1: 
#             return 0 
        
#         profit = float('-inf')
#         buy = float('inf')
        
#         for i in range(len(prices)): 
#             if prices[i] < buy: 
#                 buy = prices[i]
                
#             sell = prices[i]
#             profit = max(profit, sell - buy) 
            
                
#         return max(0, profit)
