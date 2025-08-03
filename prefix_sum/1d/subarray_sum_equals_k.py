'''
560. Subarray Sum Equals K
Link: https://leetcode.com/problems/subarray-sum-equals-k/

Resources:
- https://www.hellointerview.com/learn/code/prefix-sum/subarray-sum-equals-k
- https://www.youtube.com/watch?v=xvNwoz-ufXA
- https://www.youtube.com/watch?v=6poxiip7sBY&list=PLDMSG_DkY6zf4splOszM3iyPUeDQ_-3o5&index=11

Given an array of integers nums and an integer k
return the total number of continuous subarrays whose sum equals to k.

Examples
Input: nums = [1, 1, 1], k = 2
Output: 2

Input: nums = [1, 2, 3], k = 3
Output: 2

Input: nums = [3, 4, 7, 2, -3, 1, 4, 2], k = 7
Explanation: The subarrays that sum to 7 are:
[3, 4], [7], [7, 2, -3, 1], [1, 4, 2]
'''


# brute force solution -> time: O(n^2) space : O(1)
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

    prefix_counts = {0: 1}  # { sum: count }
    count, curr_sum = 0, 0

    for num in nums:
        curr_sum += num  # cumilative sums, s:

        # we make sure to check if the sum - k is already in the dictionary, if so, increase the count.
        rem = curr_sum - k
        if rem in prefix_counts: # meaning there's subarrays upto current index that sum to k
            count += prefix_counts[rem]

        # we check if s is already in the mapping, if so, increase by 1, if not assign 1.
        prefix_counts[num] = prefix_counts.get(curr_sum, 0) + 1

    return count

