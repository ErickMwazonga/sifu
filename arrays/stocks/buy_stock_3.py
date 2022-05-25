'''
123. Best Time to Buy and Sell Stock III
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
Credit: https://www.programcreek.com/2014/02/leetcode-best-time-to-buy-and-sell-stock-iii-java/

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


def maxProfit(prices):
    first_buy, first_sell = float('inf'), 0
    second_buy, second_sell = float('inf'), 0

    for price in prices:
        first_buy = min(first_buy, price)
        first_sell = max(first_sell, price - first_buy)

        second_buy = min(second_buy, price - first_sell)
        second_sell = max(second_sell, price - second_buy)

    return second_sell


def maxProfit_v2(prices):
    '''Two passes through the list, O(n) time, O(n) space'''

    if not prices:
        return 0

    # forward traversal, profits record the max profit
    # by the ith day, this is the first transaction
    profits = []
    current_min, max_profit = prices[0], 0

    for price in prices:
        current_min = min(current_min, price)
        max_profit = max(max_profit, price - current_min)
        profits.append(max_profit)

    # backward traversal, max_profit records the max profit
    # after the ith day, this is the second transaction
    current_max = prices[-1]
    max_profit, total_max = 0, 0

    for i in range(len(prices) - 1, -1, -1):
        current_max = max(current_max, prices[i])
        max_profit = max(max_profit, current_max - prices[i])
        total_max = max(total_max, max_profit + profits[i])

    return total_max


assert maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6
