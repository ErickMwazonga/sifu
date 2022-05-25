'''
560. Subarray Sum Equals K
Link: https://leetcode.com/problems/subarray-sum-equals-k/
Resource: https://www.youtube.com/watch?v=6poxiip7sBY&list=PLDMSG_DkY6zf4splOszM3iyPUeDQ_-3o5&index=11

Given an array of integers nums and an integer k
return the total number of continuous subarrays whose sum equals to k.

Examples
Input: nums = [1, 1, 1], k = 2
Output: 2

Input: nums = [1, 2, 3], k = 3
Output: 2
'''

from collections import defaultdict


def subarray_sum_v0(nums, k):
    count, n = 0, len(nums)

    for i in range(n):
        curr_sum = 0

        for j in range(i, n):
            curr_sum += nums[j]

            if curr_sum == k:
                count += 1

    return count


def subarray_sum(nums, k):
    # first we start from a sum which is equal to 0, and the count of it is 1.
    # this is the input list ex :   [1 4 9 -5 8] -> the sum array (s) ex : [0  1  5  13  8  16 ]

    mapping = {0: 1}  # { sum: count }
    count = our_sum = 0

    for num in nums:
        our_sum += num  # cumilative sums, s:

        # we make sure to check if the sum - k is already in the dictionary, if so, increase the count.
        if our_sum - k in mapping:
            count += mapping[our_sum - k]

        # we check if s is already in the mapping, if so, increase by 1, if not assign 1.
        mapping[num] = mapping.get(our_sum, 0) + 1

    return count


def subarray_sum_v2(nums, k):
    mapping = {0: 1}
    curr_sum, count = 0, 0

    for num in nums:
        curr_sum += num
        rem = curr_sum - k

        if rem in mapping:
            count += mapping[rem]

        mapping[curr_sum] = mapping.get(curr_sum, 0) + 1

    return count
