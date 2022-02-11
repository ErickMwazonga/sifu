'''
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in
the array, and it should return false if every element is distinct.

Examples
Input: [1,2,3,1] -> true
'''


def contains_duplicate(nums):
    freq = {}

    for num in nums:
        count = freq.get(num, 0) + 1

        if count > 1:
            return True
        freq[num] = count

    return False


assert contains_duplicate([1, 2, 3, 1]) == True
assert contains_duplicate([1, 2, 3, 4]) == False
assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
