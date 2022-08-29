'''
217. Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in
the array, and it should return false if every element is distinct.

Examples
1. [1, 2, 3, 1] -> True
2. [1, 2, 3, 4] -> False
3. [1, 1, 1, 3, 3, 4, 3, 2, 4, 2] -> True
'''


def containsDuplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))


def containsDuplicate_v2(nums: list[int]) -> bool:
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(nums)

    return False


def containsDuplicate_v3(nums: list[int]) -> bool:
    hashNum = {}

    for num in nums:
        if num in hashNum:
            return True

        hashNum[num] = 1

    return False


def contains_duplicate_v4(nums: list[int]) -> bool:
    freq = {}

    for num in nums:
        count = freq.get(num, 0) + 1

        if count > 1:
            return True

        freq[num] = count

    return False


def containsDuplicate_v5(nums: list[int]) -> bool:
    from collections import Counter

    freq = Counter(nums)
    return any(freq[num] > 1 for num in freq)


assert containsDuplicate_v2([1, 2, 3, 1]) == True
assert containsDuplicate_v2([1, 2, 3, 4]) == False
assert containsDuplicate_v2([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
