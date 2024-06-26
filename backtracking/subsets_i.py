'''
78. Subsets
Link: https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Examples:
1. [1, 2, 3] -> [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
2. [0] -> [[], [0]]
'''

class Solution:
    '''
    https://www.youtube.com/watch?v=REOH22Xwdkk&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=4
    Time Complexity: O(2^N)
    Space Complexity: O(2^N)
    '''

    def subsets(self, nums):
        res = []
        self.dfs(nums, res, subset = [], i = 0)
        return res

    def dfs(self, nums, res, subset, i):
        if i >= len(nums):
            res.append(subset[:])
            return

        # Include i
        self.dfs(nums, res, subset + [nums[i]], i + 1)

        # Exclude i
        self.dfs(nums, res, subset, i + 1)


class Solution_V1:
    '''Time: O(n*2^n)'''

    def subsets(self, nums):
        res = []
        self.dfs(nums, res, index=0, subset=[])
        return res

    def dfs(self, nums, res, index, subset):
        res.append(subset)

        for i in range(index, len(nums)):
            self.dfs(nums, res, i + 1, subset + [nums[i]])


class Solution_V2:
    '''Time: O(n*2^n)'''

    def subsets(self, nums):
        res = []
        self.dfs(nums, res, subset=[])
        return res

    def dfs(self, nums, res, subset):
        res.append(subset)

        for i in range(len(nums)):
            self.dfs(nums[i+1:], res, subset + [nums[i]])
