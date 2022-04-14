'''
645. Set Mismatch
https://leetcode.com/problems/set-mismatch/

You have a set of integers s, which originally contains all the numbers from 1 to n. 
Unfortunately, due to some error, one of the numbers in s got duplicated to another number 
in the set, which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.

Examples:
1. [1,2,2,4] -> [2,3]
3. [1,1] -> [1,2]
'''


def findErrorNums(nums):
    n = len(nums)
    true_sum = n * (n + 1) // 2

    actual_sum = sum(nums)
    set_sum = sum(set(nums))

    duplicate = actual_sum - set_sum
    miss = true_sum - set_sum

    return [duplicate, miss]
