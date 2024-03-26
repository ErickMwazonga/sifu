'''
121. Best Time to Buy and Sell Stock Say you have an array for which the ith element is the price of a given stock on day i.
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Resource: https://medium.com/algorithms-and-leetcode/best-time-to-buy-sell-stocks-on-leetcode-the-ultimate-guide-ce420259b323

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
Example 1:
[7, 1, 5, 3, 6, 4] -> 5
Explanation:
    Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Not 7-1 = 6, as selling price needs to be larger than buying price.
'''


def max_profit(prices) -> int:
    '''Linear Time, Constant Space'''

    if len(prices) <= 1:
        return 0

    min_price, max_profit = prices[0], 0
    for price in prices[1:]:
        profit = price - min_price
        min_price = min(min_price, price)
        max_profit = max(max_profit, profit)

    return max_profit


def maxProfit_v1(prices):
    if len(prices) <= 1:
        return 0
    
    min_price, max_profit = prices[0], float('-inf')
    for price in prices:
        profit = price - min_price
        min_price = min(min_price, price)
        max_profit = max(max_profit, profit)

    return max_profit


def max_profit_v2(prices) -> int:
    '''Linear Time, Constant Space'''

    n = len(prices)

    if n <= 1:
        return 0

    min_so_far, max_profit = prices[0], 0
    for price in enumerate(prices, 1):
        min_so_far = min(min_so_far, price)
        max_profit = max(max_profit, price - min_so_far)

    return max_profit

def max_profit_v3(prices: list[int]) -> int:
    '''Inspiration: https://www.youtube.com/watch?v=ioFPBdChabY'''

    profit = 0
    buy = prices[0]
    for sell in prices[1:]:
        if sell > buy:
            profit = max(profit, sell - buy)
        else:
            buy = sell
    
    return profit


assert max_profit([7, 1, 5, 3, 6, 4]) == 5
assert max_profit([7, 6, 4, 3, 1]) == 0
