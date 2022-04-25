'''
46. Permutations
https://leetcode.com/problems/permutations/

RESOURCES
1. https://www.youtube.com/watch?v=Zq4upTEaQyM
2. https://www.youtube.com/watch?v=Nabbpl7y4Lo
3. https://www.youtube.com/watch?v=DKCbsiDBN6c

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
1. [1,2,3] -> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
2. [0,1] -> [[0,1],[1,0]]
3. [1] -> [[1]]
'''


class Solution:
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return

        for i in range(len(nums)):
            # path.append(nums[i]) # doesn't work
            new_nums = nums[:i] + nums[i+1:]
            self.dfs(new_nums, path+[nums[i]], res)


class Solution2:
    def permute(self, nums):
        res, path = [], []
        visited = set()

        self.backtrack(nums, res, visited, path)
        return res

    def backtrack(self, nums, res, visited, path):
        if len(path) == len(nums):
            res.append(path)
            return

        for i in range(len(nums)):
            if i in visited:
                continue

            visited.add(i)

            self.backtrack(nums, res, visited, path + [nums[i]])
            visited.remove(i)
