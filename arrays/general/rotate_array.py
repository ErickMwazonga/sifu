'''
189. Rotate Array
https://leetcode.com/problems/rotate-array/

Given an array, rotate the array to the right by k steps, where k is non-negative.
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

Example 1:
Input: nums = [1, 2, 3, 4, 5, 6, 7],  k = 3
Output: [5, 6, 7, 1, 2, 3, 4]
Explanation:
rotate 1 steps to the right: [7, 1, 2, 3, 4, 5, 6]
rotate 2 steps to the right: [6, 7, 1, 2, 3, 4, 5]
rotate 3 steps to the right: [5, 6, 7, 1, 2, 3, 4]

Example 2:
Input: nums = [-1, -100, 3, 99],  k = 2
Output: [3, 99, -1, -100]
Explanation:
rotate 1 steps to the right: [99, -1, -100, 3]
rotate 2 steps to the right: [3, 99, -1, -100]
'''


def rotate(nums, k) -> None:
    '''Do not return anything, modify nums in-place instead'''

    temps = []
    n = len(nums)

    for i in range(n-k, n):
        temps.append(nums[i])

    for i in range(0, n-k):
        temps.append(nums[i])

    for i in range(0, len(nums)):
        nums[i] = temps[i]


assert rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]


def rotate_v2(nums, k: int) -> None:
    for _ in range(k):
        _last = nums.pop()
        nums.insert(0, _last)


def rotate_v3(nums, k) -> None:
    n = len(nums)
    temps = nums + nums
    start = n - k
    end = n + k + 1

    temps = temps[start:end]
    for i in range(n):
        nums[i] = temps[i]
