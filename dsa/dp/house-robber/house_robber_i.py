'''
198. House Robber
Link: https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them
is that adjacent houses have security system connected and it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount
of money you can rob tonight without alerting the police.

Examples
1. [1, 2, 3, 1] -> 4 => 1 + 3 = 4.
2. [2, 7, 9, 3, 1] -> 12 => 2 + 9 + 1 = 12.
'''


class Solution:
    '''PASSES'''

    def rob(self, nums: list[int]) -> int:
        return self.backtrack(nums, 0, {})

    def backtrack(self, nums: list[int], i: int, memo: dict) -> int:
        if i >= len(nums):
            return 0

        if i in memo:
            return memo[i]

        rob = nums[i] + self.backtrack(nums, i + 2, memo)
        skip = self.backtrack(nums, i + 1, memo)

        memo[i] = max(rob, skip)
        return memo[i]


class SolutionV2:
    '''FAILS'''

    def rob(self, nums: list[int]) -> int:
        return self.backtrack(nums, 0, 0, {})

    def backtrack(self, nums: list[int], total: int, i: int, memo: dict) -> int:
        if i >= len(nums):
            return total

        if i in memo:
            return memo[i]

        rob = self.backtrack(nums, total + nums[i], i + 2, memo)
        skip = self.backtrack(nums, total, i + 1, memo)

        memo[i] = max(rob, skip)
        return memo[i]



class SolutionV3:
    def rob_v3(self, nums: list[int]) -> int:
        '''Time: O(n), Space: O(n)'''

        if not nums:
            return 0

        n = len(nums)
        if n <= 2:
            return max(nums)

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            # The max if we rob it or not
            rob = nums[i] + dp[i-2]
            dont_rob = dp[i-1]
            dp[i] = max(rob, dont_rob)

        return dp[-1]


soln = Solution()
assert soln.rob([1, 2, 3, 1]) == 4
assert soln.rob([2, 7, 9, 3, 1]) == 12
