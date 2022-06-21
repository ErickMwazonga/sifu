'''
2221. Find Triangular Sum of an Array
Link: https://leetcode.com/problems/find-triangular-sum-of-an-array/

You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).
The triangular sum of nums is the value of the only element present in nums after the following process terminates:

Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1.
For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator.
Replace the array nums with newNums.
Repeat the entire process starting from step 1.
Return the triangular sum of nums.

Examples:
1. [1, 2, 3, 4, 5] -> 8
2. [5] -> 5
'''


def triangularSum(nums: list[int]) -> int:
    if len(nums) == 1:
        return sum(nums)

    while len(nums) > 1:
        curr_nums = []

        for i in range(1, len(nums)):
            left_sum = nums[i-1] + nums[i]
            left_sum %= 10
            curr_nums.append(left_sum)

        nums = curr_nums

    return nums[0]


def triangularSum_v2(nums: list[int]) -> int:
    n = len(nums)

    while n > 0:
        for i in range(n-1):
            right_sum = nums[i] + nums[i+1]
            nums[i] = right_sum % 10
        n -= 1

    return nums[0]
