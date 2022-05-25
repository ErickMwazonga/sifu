'''
448. Find All Numbers Disappeared in an Array
Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
Similar: Link: https://leetcode.com/problems/first-missing-positive/

Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.

Examples:
1. [4, 3, 2, 7, 8, 2, 3, 1] -> [5, 6]
2. [1, 1] -> [2]
 
Follow up: Could you do it without extra space and in O(n) runtime? 
You may assume the returned list does not count as extra space.
'''


def findDisappearedNumbers(nums):
    existing = set(nums)
    res = []

    for i in range(1, len(nums)+1):
        if i not in existing:
            res.append(i)

    return res


def findDisappearedNumbers_v2(nums):
    return set(range(1, len(nums) + 1)) - set(nums)


def findDisappearedNumbers_v3(nums):
    # mark existing
    for n in nums:
        i = abs(n) - 1
        nums[i] = -1 * abs(nums[i])

    res = []
    for i, n in enumerate(nums):
        if n > 0:
            res.append(i+1)

    return res


assert findDisappearedNumbers_v3([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
assert findDisappearedNumbers_v3([1, 1]) == [2]
