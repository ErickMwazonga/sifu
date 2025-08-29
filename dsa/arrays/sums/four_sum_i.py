'''
18. 4Sum
Link: https://leetcode.com/problems/4sum/

Given an array nums of n integers, return an array of all the unique 
quadruplets [nums[a], nums[b], nums[c], nums[d]] 
such that: 
    1. 0 <= a, b, c, d < n
    2. a, b, c, and d are distinct.
    3. nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1, 0, -1, 0, -2, 2],  target = 0
Output: [[-2, -1, 1, 2],  [-2, 0, 0, 2],  [-1, 0, 0, 1]]

Example 2:
Input: nums = [2, 2, 2, 2, 2], target = 8
Output: [[2, 2, 2, 2]]
'''

def fourSum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    n, quadruplets = len(nums), set()

    for i in range(n):
        for j in range(i + 1, n):
            left, right = j + 1, n - 1

            while left < right:
                curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if curr_sum == target:
                    quadruplets.add((nums[i], nums[j], nums[left], nums[right]))
                    left, right = left + 1, right - 1
                elif curr_sum < target:
                    left += 1 
                else:
                    right -= 1
                    
    return list(quadruplets)

class Solution_V2:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res = set()

        self.ksum(nums, res, [], 4, 0, target)
        return [list(tup) for tup in res]


    def ksum(self, nums, res, curr, k, start, target):
        if k == 2:
            left, right = start, len(nums) - 1
            while left < right:
                curr_sum = nums[left] + nums[right]
                if  curr_sum == target:
                    res.add(tuple(curr + [nums[left], nums[right]]))
                    left, right = left + 1, right - 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
        else:
            for i in range(start, len(nums) - k + 1):
                self.ksum(nums, res, curr + [nums[i]], k - 1, i + 1, target - nums[i])


class Solution_V3:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res = set()
        self.ksum(nums, res, [], 4, 0, target)
        return [list(tup) for tup in res]

    def ksum(self, nums, res, curr, k, start, target):
        if k == 2:
            self.two_sum(nums, res, curr, start, target)
        else:
            for i in range(start, len(nums) - k + 1):
                self.ksum(nums, res, curr + [nums[i]], k - 1, i + 1, target - nums[i])

    def two_sum(self, nums, res, curr, start, target):
        left, right = start, len(nums) - 1
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == target:
                res.add(tuple(curr + [nums[left], nums[right]]))
                left, right = left + 1, right - 1
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
