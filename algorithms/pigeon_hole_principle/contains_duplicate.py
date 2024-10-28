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

# PIGEON HOLE PRINCIPLE
# --------------------------
# The pigeonhole principle states that if you have n pigeons and k pigeonholes such that n > k,
# then atleast one pigeonhole will have more than one pigeon. Using the same principle, we can say the following


def containsDuplicate(nums: list[int]) -> bool:
    if not nums:
        return False

    n_unique_nums = len(set(nums))  # Pigeons
    n = len(nums) # Pigeonholes

    return n_unique_nums // n == 0


assert containsDuplicate([1, 2, 3, 1]) == True
assert containsDuplicate([1, 2, 3, 4]) == False
assert containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
