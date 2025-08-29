'''
930. Binary Subarrays With Sum
https://leetcode.com/problems/binary-subarrays-with-sum/description/

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
A subarray is a contiguous part of the array.

Example 1:
Input: nums = [1, 0, 1, 0, 1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:
Input: nums = [0, 0, 0, 0, 0], goal = 0
Output: 15
'''

def numSubarraysWithSum(nums: list[int], goal: int) -> int:
    prefix_counts = {0: 1}
    curr_sum, total_subarrays= 0, 0
    
    for num in nums:
        curr_sum += num

        rem = curr_sum - goal
        if rem in prefix_counts:
            total_subarrays += prefix_counts[rem]

        prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1

    return total_subarrays
