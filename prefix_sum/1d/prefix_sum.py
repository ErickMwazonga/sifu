'''
1480. Running Sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example 1:
Input: nums = [1, 2, 3, 4]
Output: [1, 3, 6, 10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [1, 1, 1, 1, 1]
Output: [1, 2, 3, 4, 5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3, 1, 2, 10, 1]
Output: [3, 4, 6, 16, 17]
'''

def runningSum(nums: list[int]) -> list[int]:
    for i in range(1,len(nums)):
        nums[i] += nums[i - 1]
    return nums

def runningSum(nums: list[int]) -> list[int]:
    result = []
    total = 0
    for num in nums:
        total += num
        result.append(total)
    return result

def runningSum(nums: list[int]) -> list[int]:
    sums = []
    for i in range(len(nums)):
        if i == 0:
            sums.append(nums[i])
        else:
            sums.append(sums[i - 1] + nums[i])
    return sums
