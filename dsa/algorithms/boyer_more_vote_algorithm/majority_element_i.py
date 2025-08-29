'''
169. Majority Element
Link: https://leetcode.com/problems/majority-element/

Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Examples
1. [3, 2, 3] -> 3
2. [2, 2, 1, 1, 1, 2, 2] -> 2
'''


def majority_element(nums: list[int]) -> int:
    counter = {}
    majority = len(nums) // 2

    for num in nums:
        counter[num] = counter.get(num, 0) + 1

    for k, v in counter.items():
        if v > majority:
            return k

    return -1


def majorityElement_v1(nums: list[int]) -> int:
    '''
    Boyer Moore Majority Voting algorithm
    The Boyer-Moore majority vote algorithm is an algorithm for finding the majority of a
    sequence of elements using linear time and constant space.
    '''
    counter, majority = 1, nums[0]

    for num in nums[1:]:
        if counter == 0:
            majority = num

        counter += 1 if num == majority else -1

    return majority


def majority_element_v2(nums: list[int]) -> int:
    counter, majority = 1, nums[0]

    for num in nums[1:]:
        if num == majority:
            counter += 1
        else:
            counter -= 1

        if counter == 0:
            majority = num
            counter = 1

    return majority


assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
assert majority_element([3, 2, 3]) == 3
