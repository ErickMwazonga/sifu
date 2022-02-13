'''
268. Missing Number
https://leetcode.com/problems/missing-number/
https://www.geeksforgeeks.org/find-the-missing-number/

You are given a list of n-1 integers and these integers are in the range of 1 to n.
There are no duplicates in the list. One of the integers is missing in the list. 
Write an efficient code to find the missing integer.

Examples:
1. [1, 2, 4, 6, 3, 7, 8] -> 5
2. [1, 2, 3, 5] -> 4
'''


def missing_number(nums):
    n = len(nums)
    visited = set(nums)

    for i in range(1, n + 2):
        if i not in visited:
            return i


def get_missing(A):
    n = len(A) + 1
    total = n * (n + 1) // 2

    sum_of_A = sum(A)
    return total - sum_of_A


# Find missing between two given sets
def find_missing(full_list, partial_list):
    missing_nums = set(full_list) - set(partial_list)
    assert(len(missing_nums) == 1)
    return list(missing_nums)[0]


def find_missing(full_list, partial_list):
    return sum(full_list) - sum(partial_list)


assert find_missing([0, 1, 2, 4, 5, 6]) == 7
assert find_missing([3, 0, 1]) == 2
assert find_missing([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
