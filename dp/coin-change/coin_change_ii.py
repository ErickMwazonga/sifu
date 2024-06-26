'''
518. Coin Change 2
Link: https://leetcode.com/problems/coin-change-2/

You are given an integer array coins representing coins of different denominations and
an integer amount representing a total amount of money.
Return the number of combinations that make up that amount.
If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.

Example:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5 = 5
5 = 2 + 2 + 1
5 = 2 + 1 + 1 + 1
5 = 1 + 1 + 1 + 1 + 1
'''


class Solution:
    def change(self, amount, coins):
        return self.dfs(coins, amount, i=0, memo={})

    def dfs(self, coins, amount, i, memo):
        if amount == 0:
            return 1

        if amount < 0 or i == len(coins):
            return 0

        if (i, amount) in memo:
            return memo[(i, amount)]

        include = self.dfs(coins, amount - coins[i], i, memo)
        exclude = self.dfs(coins, amount, i + 1, memo)

        memo[(i, amount)] = include + exclude
        return memo[(i, amount)]


class Solution_V2:
    def change(self, amount, coins):
        return self.dfs(amount, coins, i=0, target=0, cache={})

    def dfs(self, amount, coins, i, target, cache):
        if target == amount:
            return 1

        if target > amount:
            return 0

        if i == len(coins):
            return 0

        if (i, target) in cache:
            return cache[(i, target)]

        include = self.dfs(amount, coins, i, target + coins[i], cache)
        exclude = self.dfs(amount, coins, i + 1,  target, cache)

        cache[(i, target)] = include + exclude
        return cache[(i, target)]
