'''
268. Missing Number
Link: https://leetcode.com/problems/missing-number/

Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Examples:
1. [1, 2, 4, 6, 3, 7, 8] -> 5
2. [1, 2, 3, 5] -> 4
3. [3, 0, 1] -> 2
4. [0, 1] -> 2
5. [9, 6, 4, 2, 3, 5, 7, 0, 1] -> 8
'''


def missingNumber(nums: list[int]) -> int:
    n = len(nums)
    visited = set(nums)

    for i in range(0, n + 1):
        if i not in visited:
            return i

    return -1


def missingNumber_v2(nums: list[int]) -> int:
    n = len(nums)
    cummulative_sum = sum(range(n+1))
    return cummulative_sum - sum(nums)


def missingNumber_v3(nums: list[int]) -> int:
    n = len(nums)
    cummulative_sum = n * (n + 1) // 2

    return cummulative_sum - sum(nums)


assert missingNumber([0, 1, 2, 4, 5, 6]) == 7
assert missingNumber([3, 0, 1]) == 2
assert missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
