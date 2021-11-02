'''
78. Subsets
https://leetcode.com/problems/subsets/

Given an integer array nums, return all possible subsets (the power set).

The solution set must not contain duplicate subsets.
Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
'''


def subsets(nums):
    '''2^n'''
    output = [[]]

    for num in nums:
        # output += [lst + [num] for lst in output]
        for i in range(len(res)):
            output.append(res[i] + [num])

    return output

# REQUIRE REVISION


class Solution(object):
    def subsets(self, nums):
        ret = []
        self.dfs(nums, [], ret)
        return ret

    def dfs(self, nums, path, ret):
        ret.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], path+[nums[i]], ret)

# REQUIRE REVISION


class Solution(object):
    def subsets(self, nums):
        sol = []
        self.helper(nums, sol, [], 0)
        return sol

    def helper(self, nums, sol, curr, index):
        sol.append(list(curr))

        for i in range(index, len(nums)):
            curr.append(nums[i])
            self.helper(nums, sol, curr, i + 1)
            curr.pop()
