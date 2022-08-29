'''
41. First Missing Positive
Link: https://leetcode.com/problems/first-missing-positive/
Related: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Given an unsorted integer array, find the smallest missing positive integer.

Examples:
1. [1, 2, 0] -> 3
2. [3, 4, -1, 1] ->  2
3. [7, 8, 9, 11, 12] -> 1

Your algorithm should run in O(n) time and uses constant extra space.
But the time complexity is O(n), because membership check in a set is O(1)
and the for loop complexity is O(n) (same for array to set()).
therefore the overall asymptotic time complexity is O(n).
'''


def first_missing_positive(nums: list[int]) -> int:
    n, visisted = len(nums), set(nums)

    for i in range(1, n + 2):
        if i not in visisted:
            return i


def firstMissingPositive_v1(nums: list[int]) -> int:
    n = len(nums)

    for i in range(n):
        if nums[i] <= 0:
            nums[i] = n + 1

    for num in nums:
        if abs(num) > n:
            continue

        idx = abs(num) - 1
        nums[idx] = -abs(nums[idx])

    for i in range(n):
        if nums[i] > 0:
            return i + 1

    return n + 1


def first_missing_positive_v2(nums: list[int]) -> int:
    n = len(nums)

    # cleaning up the array (negative nos + nos > n)
    for idx in range(n):
        if nums[idx] <= 0 or nums[idx] > n:
            nums[idx] = n + 1

    # placing our marker to see what numbers have been accounted for
    for num in nums:
        num = abs(num)

        if num <= n and nums[num - 1] >= 0:
            nums[num - 1] *= -1

    # final step for getting the answer
    for idx in range(n):
        if nums[idx] > 0:
            return idx + 1

    return n + 1


assert first_missing_positive_v2([1, 2, 0]) == 3
assert first_missing_positive_v2([3, 4, -1, 1]) == 2
assert first_missing_positive_v2([7, 8, 9, 11, 12]) == 1
