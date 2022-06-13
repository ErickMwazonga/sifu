'''
416. Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/

Given a non-empty array nums containing only positive integers, find if the array can be partitioned 
into two subsets such that the sum of elements in both subsets is equal.

Examples:
1. [1, 5, 11, 5] -> True
    Explanation: The array can be partitioned as [1, 5, 5] and [11].

2. [1, 2, 3, 5] -> False
    Explanation: The array cannot be partitioned into equal sum subsets.
'''


class Solution:
    def canPartition(self, nums) -> bool:
        total = sum(nums)
        target, rem = divmod(total, 2)

        if rem != 0:
            return False

        return self.dfs(nums, target, 0, memo={})

    def dfs(self, nums, target, i, memo):
        key = (i, target)

        if key in memo:
            return memo[key]

        if i >= len(nums):
            return False

        if target == 0:
            return True

        include = self.dfs(nums, target-nums[i], i+1, memo)
        exclude = self.dfs(nums, target, i+1, memo)

        memo[key] = include or exclude

        return memo[key]


class Solution_V2:
    def canPartition(self, nums):
        total = sum(nums)
        target, rem = divmod(total, 2)

        if rem != 0:
            return False

        return self.dfs(nums, target, 0, memo={})

    def dfs(self, nums, target, i, memo):
        if (i, target) in memo:
            return memo[(i, target)]

        if target < 0:
            return

        if target == 0:
            return True

        for j in range(i, len(nums)):
            if self.dfs(nums, target-nums[j], j+1, memo):
                return True

        memo[(i, target)] = False
        return False
