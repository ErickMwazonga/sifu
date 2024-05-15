'''
322. Coin Change
Link: https://leetcode.com/problems/coin-change/
Resource: https://www.youtube.com/watch?v=H9bfqozjoqs
Resource: https://randomwits.com/blog/coin-change-leetcode-solution

You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Examples
1. coins = [1, 2, 5], amount = 11 -> Output: 3 => 11 = 5 + 5 + 1
2. coins = [2], amount = 3 -> Output: -1
3. coins = [1], amount = 0 -> Output: 0
4. coins = [1], amount = 1 -> Output: 1
5. coins = [1], amount = 2 -> Output: 2
'''


class Solution:
    _MAX = float('inf')

    def coinChange(self, coins: list[int], amount: int) -> float:
        result = self.backtrack(coins, amount, {})
        return result if result != self._MAX else -1

    def backtrack(self, coins: list[int], amount: int, memo: dict) -> float:
        if amount == 0:
            return 0

        if amount < 0:
            return self._MAX

        if amount in memo:
            return memo[amount]

        min_coins = self._MAX
        for coin in coins:
            # use coin and check the rest of the remaining coins
            # note -> adding 1 to MAX doesn't change the max value
            use_coin = 1 + self.backtrack(coins, amount - coin, memo)
            min_coins = min(min_coins, use_coin)

        memo[amount] = min_coins
        return memo[amount]
