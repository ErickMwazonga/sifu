'''
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in
the array, and it should return false if every element is distinct.

Examples
1. [1, 2, 3, 1] -> true
2. [1, 2, 3, 4] -> False
3. [1, 1, 1, 3, 3, 4, 3, 2, 4, 2] -> True
'''


def containsDuplicate(nums):
    return len(nums) != len(set(nums))


def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(nums)

    return False


def containsDuplicate2(nums):
    hashNum = {}

    for num in nums:
        if num in hashNum:
            return True
        hashNum[num] = 1

    return False


def contains_duplicate(nums):
    freq = {}

    for num in nums:
        count = freq.get(num, 0) + 1

        if count > 1:
            return True
        freq[num] = count

    return False


def containsDuplicate3(nums):
    from collections import Counter

    freq = Counter(nums)
    for _, freq in freq.items():
        if freq > 1:
            return True

    return False


assert contains_duplicate([1, 2, 3, 1]) == True
assert contains_duplicate([1, 2, 3, 4]) == False
assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
