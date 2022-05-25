'''
189. Rotate Array
Link: https://leetcode.com/problems/rotate-array/

Given an array, rotate the array to the right by k steps, where k is non-negative.
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

Example 1:
Input: nums = [1, 2, 3, 4, 5, 6, 7],  k = 3
Output: [5, 6, 7, 1, 2, 3, 4]
Explanation:

Example 2:
Input: nums = [-1, -100, 3, 99],  k = 2
Output: [3, 99, -1, -100]
'''


def rotate(nums, k: int) -> None:
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]


def rotate_v2(self, nums, k):
    n = len(nums)
    new_nums = [0] * n

    for i in range(n):
        idx = (i + k) % n
        new_nums[idx] = nums[i]

    for i in range(n):
        nums[i] = new_nums[i]


class Solution_V3:
    def rotate(self, nums, k) -> None:
        n = len(nums)

        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def reverse(self, nums, start, end) -> None:
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
