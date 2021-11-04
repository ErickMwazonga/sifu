'''
70. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: 2 ->  2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3 -> 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''


class Solution:
    '''
    The total distinct ways to climb to i th stair is actually the
    sum of the distinct ways of i – 2 and i – 1 stairs.

    Time complexity: O(n). Single loop up to n.
    Space complexity: O(n). dp array of size n is used.
    '''

    def climbStairs(self, n):
        ways = [1, 2]

        for i in range(2, n):
            distinct_ways = ways[i-1] + ways[i-2]
            ways.append(distinct_ways)

        return ways[n - 1]

    def fib(n):
        dp = [0] * n

        for i in range(n):
            if i <= 2:
                dp[i] = i + 1
            else:
                dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]
