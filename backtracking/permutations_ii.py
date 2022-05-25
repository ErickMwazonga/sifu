'''
47. Permutations II
Link: https://leetcode.com/problems/permutations-ii/

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Examples:
1. [1,1,2] -> [[1,1,2], [1,2,1], [2,1,1]]
2. [1,2,3] -> [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
'''

from collections import Counter


class Solution:
    def permuteUnique(self, nums):
        nums.sort()

        res, path = [], []
        self.dfs(nums, path, res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            new_nums = nums[:i] + nums[i+1:]
            self.dfs(new_nums, path+[nums[i]], res)


class Solution_V2:
    def permuteUnique(self, nums):
        res, path = set(), []
        visited = set()

        self.backtrack(nums, res, visited, path)
        return [list(path) for path in res]

    def backtrack(self, nums, res, visited, path):
        if len(path) == len(nums):
            res.add(tuple(path))  # list is not hashable hence a tuple
            return

        for i in range(len(nums)):
            if i in visited:
                continue

            visited.add(i)

            self.backtrack(nums, res, visited, path + [nums[i]])
            visited.remove(i)
