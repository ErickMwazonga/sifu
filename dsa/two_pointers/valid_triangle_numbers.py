'''
611. Valid Triangle Number
https://leetcode.com/problems/valid-triangle-number/

Given an integer array nums, return the number of triplets chosen from the array that can make triangles
if we take them as side lengths of a triangle.

Example 1:
Input: nums = [2, 2, 3, 4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Example 2:
Input: nums = [4, 2, 3, 4]
Output: 4
'''

def triangleNumber(nums: list[int]) -> int:
    nums.sort()
    n = len(nums)
    res = 0

    for k in range(n - 1, 1, -1): # fix the largest side
        left, right = 0, k - 1
        while left < right:
            if nums[left] + nums[right] > nums[k]:
                res += right - left # all pairs (left...right-1, j) are valid
                right -= 1
            else:
                left += 1
    return res