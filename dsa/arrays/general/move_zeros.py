'''
283. Move Zeroes
Link: https://leetcode.com/problems/move-zeroes/
Resource: https://leetcode.com/problems/move-zeroes/discuss/979820/Two-Pointeror-Visual-or-Python

Given an array nums, write a function to move all 0's to the end of
it while maintaining the relative order of the non-zero elements.

Examples:
1. [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
2. [0] -> [0]

Note: Do this in-place without making a copy of the array.
'''


def move_zeroes(nums) -> None:
    '''Do not return anything, modify nums in-place instead'''

    i, n = 0, len(nums)

    for j in range(n):
        if nums[j] == 0:
            continue

        nums[i], nums[j] = nums[j], nums[i]
        i += 1


def move_zeroes_v2(nums) -> None:
    '''Do not return anything, modify nums in-place instead.'''

    i, j = 0, 1

    while j < len(nums):
        if nums[i] == 0 and nums[j] == 0:
            j += 1
            continue

        if nums[i] == 0 and nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]

        i += 1
        j += 1


def move_zeroes_v3(nums) -> None:
    left, right = 0, 1

    while right < len(nums):
        if nums[left] == 0 and nums[right] == 0:
            right += 1
        elif nums[left] != 0 and nums[right] != 0:
            left += 1
            right += 1
        elif nums[left] == 0 and nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1


assert move_zeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
