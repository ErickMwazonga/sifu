'''
229. Majority Element II
Link: https://leetcode.com/problems/majority-element-ii/

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Follow-up: Could you solve the problem in linear time and in O(1) space?

Examples
1. [3, 2, 3] -> [3]
2. [1] -> [1]
3. [1, 2] -> [1, 2]
'''


def majority_element(nums):
    # There can only be 2 or less majority elements

    cand1, count1 = None, 0
    cand2, count2 = None, 0

    for num in nums:
        if num == cand1:
            count1 += 1
        elif num == cand2:
            count2 += 1
        elif count1 == 0:
            cand1 = num
            count1 += 1
        elif count2 == 0:
            cand2 = num
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1

    # return [x for x in (cand1, cand2) if nums.count(x) > len(nums) // 3]

    # Get the candidate no of occurrences
    count1, count2 = 0, 0
    for num in nums:
        if num == cand1:
            count1 += 1
        elif num == cand2:
            count2 += 1

    # Verify if indeed they have occurrences greate than n/3
    ans = []
    athird = len(nums) / 3
    if count1 > athird:
        ans.append(cand1)

    if count2 > athird:
        ans.append(cand2)

    return ans


assert majority_element([1, 2]) == [1, 2]
