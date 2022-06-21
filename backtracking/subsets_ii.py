'''
90. Subsets II
Link: https://leetcode.com/problems/subsets-ii/

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
1. [1, 2, 2] -> [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
2. [0] -> [[], [0]]
'''


class Solution:
    '''Time: O(n*2^n)'''

    def subsets(self, nums):
        nums.sort()

        res, subset = [], []
        self.dfs(nums, res, 0, subset)
        return res

    def dfs(self, nums, res, index, subset):
        res.append(subset)

        for i in range(index, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            self.dfs(nums, res, i+1, subset+[nums[i]])


class Solution_V2:
    def subsetsWithDup(self, nums):
        nums.sort()

        res, subset = [], []
        self.dfs(nums, res, subset)
        return res

    def dfs(self, nums, subset, res):
        res.append(subset)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            self.dfs(nums[i+1:], res, subset + [nums[i]])


class Solution_V3:
    def subsetsWithDup(self, nums):
        res, subset = [], []
        nums.sort()

        self.dfs(nums, subset, res, 0)

        return res

    def dfs(self, nums, subset, res, i):
        if i >= len(nums):
            res.append(subset)
            return

        # Include i
        subset.append(nums[i])
        self.dfs(nums, subset, res, i + 1)
        subset.pop()

        # Exclude i
        while i + 1 < len(nums) and nums[i] == nums[i+1]:
            i += 1

        self.dfs(nums, subset, res, i + 1)
