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

    for l in range(n):
        for i in range(l + 1, n):
            j = i + 1
            k = n - 1

            while j < k:
                curr_sum = nums[j] + nums[k] + nums[l] + nums[i]
                if curr_sum < target:
                    j += 1 
                elif curr_sum > target:
                    k -= 1
                elif curr_sum == target:
                    quadruplets.add((nums[l], nums[i], nums[j], nums[k]))
                    j, k = j + 1, k - 1
                    
    return list(quadruplets)