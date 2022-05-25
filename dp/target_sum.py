'''
494. Target Sum
Link: https://leetcode.com/problems/target-sum/

You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' 
before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' 
before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example 1:
Input: nums = [1, 1, 1, 1, 1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1
'''


class Solution:
    '''Time: 2^n'''

    def findTargetSumWays(self, nums, target):
        if not nums:
            return 0

        return self.dfs(nums, target, index=0, total=0)

    def dfs(self, nums, target, index, total):
        if index == len(nums):
            return 1 if target == total else 0

        include = self.dfs(nums, target, index + 1, total + nums[index])
        exclude = self.dfs(nums, target, index + 1, total - nums[index])

        return include + exclude


class Solution_V2:
    '''Time: N*M - size of nums * range of sums'''

    def findTargetSumWays(self, nums, target):
        if not nums:
            return 0

        return self.dfs(nums, target, index=0, total=0, memo={})

    def dfs(self, nums, target, index, total, memo):
        if index == len(nums):
            return 1 if target == total else 0

        if (index, total) in memo:
            return memo[(index, total)]

        include = self.dfs(nums, target, index + 1, total + nums[index], memo)
        exclude = self.dfs(nums, target, index + 1, total - nums[index], memo)

        res = include + exclude
        memo[(index, total)] = res
        return res
