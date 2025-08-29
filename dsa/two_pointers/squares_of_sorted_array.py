'''
977. Squares of a Sorted Array
Link: https://leetcode.com/problems/squares-of-a-sorted-array/

Given an array of integers A sorted in non-decreasing order,
return an array of the squares of each number,also in sorted non-decreasing order.

Examples:
1. [-4, -1, 0, 3, 10] -> [0, 1, 9, 16, 100]
2. [-7, -3, 2, 3, 11] -> [4, 9, 9, 49, 121]
'''



def sortedSquares(nums: list[int]) -> list[int]:
    '''Time - O(NlogN)'''

    return sorted(map(lambda x: x ** 2, nums))


def sortedSquares_v2( nums: list[int]) -> list[int]:
    '''Time - O(N)'''

    res = []
    left, right = 0, len(nums) - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            res.append(nums[left] ** 2)
            left += 1
        else:
            res.append(nums[right] ** 2)
            right -= 1

    return res[::-1]



assert sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
assert sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
