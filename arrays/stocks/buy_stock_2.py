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


def max_profit(prices) -> int:
    n = len(prices)

    if n <= 1:
        return 0

    max_profit = 0

    for i in range(1, n):
        prev_price = prices[i - 1]

        if prices[i] > prev_price:
            profit = prices[i] - prev_price
            max_profit += profit

    return max_profit


assert max_profit([7, 1, 5, 3, 6, 4]) == 7
assert max_profit([1, 2, 3, 4, 5]) == 4
assert max_profit([7, 6, 4, 3, 1]) == 0
