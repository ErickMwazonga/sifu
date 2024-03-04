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

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        results = []
        self.helper(nums, target, 4, [], results)
        return results
    
    def helper(self, nums, target, N, res, results):
        if len(nums) < N or N < 2:
            return
        
        if N == 2:
            output_2sum = self.twoSum(nums, target)
            if output_2sum != []:
                for idx in output_2sum:
                    results.append(res + idx)
        
        else: 
            for i in range(len(nums) - N + 1):
                if nums[i] * N > target or nums[-1] * N < target:
                    break
                if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                    self.helper(
                        nums[i+1:], target-nums[i], N-1, res + [nums[i]], results
                    )
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        res = []
        left, right = 0, len(nums) - 1 

        while left < right: 
            temp_sum = nums[left] + nums[right] 

            if temp_sum == target:
                res.append([nums[left], nums[right]])
                left, right = left + 1, right - 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while right > left and nums[right] == nums[right + 1]:
                    right -= 1
            elif temp_sum < target: 
                left +=1 
            else: 
                right -= 1
                                        
        return res