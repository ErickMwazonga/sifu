'''
698. Partition to K Equal Sum Subsets
Link: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
Resource: https://www.youtube.com/watch?v=mBk4I0X46oI

Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.
 
Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:
Input: nums = [1, 2, 3, 4], k = 3
Output: false
'''


class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        if k == 1:
            return True

        n, total = len(nums), sum(nums)

        if total % k != 0:
            return False

        nums.sort(reverse=True)
        target = total // k

        if nums[0] > target:
            return False

        visited = [False] * n

        return self.dfs(nums, target, visited, k, 0, 0)

    def dfs(self, nums, target, visited, k, subset_sum, i):
        if k == 0:
            return True

        if subset_sum > target:
            return False

        if subset_sum == target:
            return self.dfs(nums, target, visited, k-1, 0, 0)

        for j in range(i, len(nums)):
            if visited[j]:
                continue

            if (subset_sum + nums[j]) > target:
                continue

            visited[j] = True
            if self.dfs(nums, target, visited, k, subset_sum + nums[j], i+1):
                return True

            visited[j] = False

        return False
