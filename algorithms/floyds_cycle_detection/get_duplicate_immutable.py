'''
287. Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/

Credit: https://www.youtube.com/watch?v=dfIqLxAf-8s
Credit: https://bit.ly/3NtUh1I

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Examples
1. [1, 3, 4, 2, 2] -> 2
2. [3, 1, 3, 4, 2] -> 3
'''


def find_duplicate(nums) -> int:
    slow = nums[0]
    fast = nums[slow]

    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    slow = nums[0]
    while slow != fast:
        slow, fast = nums[slow], nums[fast]

    return slow
