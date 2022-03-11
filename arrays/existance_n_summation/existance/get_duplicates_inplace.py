'''
Find duplicates in O(n) time and O(1) extra space

Given an array of n elements which contains elements from 0 to n-1,
with any of these numbers appearing any number of times.
Find these repeating numbers in O(n) and using only constant memory space.
Key factor here array is of length n and has elements from 0 to n-1.

Example 1
Input : n = 7 and array = [1, 2, 3, 1, 3, 6, 6]
Output: [1, 3, 6]

Example 2
Input : n = 5 and array = [1, 2, 3, 4 ,3]
Output: [3]
'''


def duplicate_positions(nums):
    res = []

    for v in nums:
        pos = abs(v) - 1

        if nums[pos] < 0:
            res.append(pos + 1)

        nums[pos] = -nums[pos]

    return res


nums = [4, 3, 2, 7, 8, 2, 3, 1]
assert duplicate_positions(nums) == [2, 3]
