'''
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''


def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0

    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1


def moveZeroes2(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i, j = 0, 1

    while j < len(nums):
        if nums[i] == 0 and nums[j] == 0:
            j += 1
            continue

        if nums[i] == 0 and nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]

        i += 1
        j += 1


def moveZeroes(nums) -> None:
    left, right = 0, 1

    while right < len(nums):
        if nums[left] == 0 and nums[right] == 0:
            right += 1
        elif nums[left] != 0 and right != 0:
            left += 1
            right += 1
        elif nums[left] == 0 and nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1


nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
# Output: [1,3,12,0,0]
print(nums)
