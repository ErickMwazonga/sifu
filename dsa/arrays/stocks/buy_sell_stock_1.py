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

INTUITION
- Preprocessing -> right to left -> get max so far from right to
'''


def max_profit(prices: list[int]) -> int:
    # pre-processing
    max_from_right = [float('-inf')]
    for i in range(len(prices) - 1, -1, -1):
        last_max = max_from_right[-1]
        max_from_right.append(max(last_max, prices[i]))
    
    max_from_right = max_from_right[1:][::-1]
    max_profit = 0
    for i in range(len(prices) - 1):
        profit = max_from_right[i + 1] - prices[i] 
        max_profit = max(max_profit, profit)

    return max_profit

def max_profit_v2(prices: list[int]) -> int:
    max_so_far, max_profit = float('-inf'), float('-inf')
    for price in reversed(prices):
        max_so_far = max(max_so_far, price)
        max_profit = max(max_profit, max_so_far - price)
    return max_profit


assert max_profit([7, 1, 5, 3, 6, 4]) == 5
assert max_profit([7, 6, 4, 3, 1]) == 0
