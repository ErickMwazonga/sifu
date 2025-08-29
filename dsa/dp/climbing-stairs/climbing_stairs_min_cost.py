'''
746. Min Cost Climbing Stairs
Link - https://leetcode.com/problems/min-cost-climbing-stairs/

You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
'''

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        min_cost_starting_0 = self.dfs(cost, 0, memo = {})
        min_cost_starting_1 = self.dfs(cost, 1, memo = {})

        return min(min_cost_starting_0, min_cost_starting_1)

    def dfs(self, cost: list[int], i: int, memo: dict) -> int:
        if i >= len(cost):
            return 0

        if i in memo:
            return memo[i]

        take_one_step = cost[i] + self.dfs(cost, i + 1, memo)
        take_two_steps = cost[i] + self.dfs(cost, i + 2, memo)

        memo[i] = min(take_one_step, take_two_steps)
        return memo[i]

class SolutionV1:

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        min_cost_starting_0 = self.dfs(cost, 0, 0, memo = {})
        min_cost_starting_1 = self.dfs(cost, 1, 0, memo = {})

        return min(min_cost_starting_0, min_cost_starting_1)

    def dfs(self, cost: list[int], i: int, total: int, memo: dict) -> int:
        if i >= len(cost):
            return total

        if (i, total) in memo:
            return memo[(i, total)]

        take_one_step = self.dfs(cost, i + 1, total + cost[i], memo)
        take_two_steps = self.dfs(cost, i + 2, total + cost[i], memo)

        memo[(i, total)] = min(take_one_step, take_two_steps)
        return memo[(i, total)]
