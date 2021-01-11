'''
322. Coin Change
https://leetcode.com/problems/coin-change/
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Examples
Input: coins = [1,2,5], amount = 11 -> Output: 3 ------> 11 = 5 + 5 + 1
Input: coins = [2], amount = 3 -> Output: -1 
Input: coins = [1], amount = 0 -> Output: 0
Input: coins = [1], amount = 1 -> Output: 1
Input: coins = [1], amount = 2 -> Output: 2
'''


class Solution(object):
    '''
    Time complexity: ~N*M, M is amount
    Space complexity: ~M, M is amount
    '''

    def coinChange(self, coins, amount):
        MAX = float('inf')
        dp = [0] + [MAX] * amount
        
        for i in range(0, amount + 1):
            for coin in coins:
                balance = i - coin

                if balance >= 0:
                    dp[i] = min(dp[i], dp[balance] + 1)
        
        if dp[amount] == MAX:  
            return -1

        return dp[-1]