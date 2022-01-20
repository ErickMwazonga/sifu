'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
https://medium.com/algorithms-and-leetcode/best-time-to-buy-sell-stocks-on-leetcode-the-ultimate-guide-ce420259b323
121. Best Time to Buy and Sell Stock Say you have an array for which the ith element
is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
Example 1:
[7, 1, 5, 3, 6, 4] -> 5
Explanation:
    Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
[7, 6, 4, 3, 1] -> 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''


def maxProfit(prices) -> int:
    '''Linear Time, Constant Space'''

    n = len(prices)

    if n <= 1:
        return 0

    min_stock, max_profit = prices[0], float('-inf')

    for price in prices:
        profit = price - min_stock
        min_stock = min(min_stock, price)
        max_profit = max(max_profit, profit)

    return max_profit


def maxProfit2(prices) -> int:
    '''Linear Time, Constant Space'''

    n = len(prices)

    if n <= 1:
        return 0

    min_so_far, max_profit = prices[0], 0

    for price in enumerate(prices, 1):
        min_so_far = min(min_so_far, price)
        max_profit = max(max_profit, price - min_so_far)

    return max_profit


assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert maxProfit([7, 6, 4, 3, 1]) == 0
