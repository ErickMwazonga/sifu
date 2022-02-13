'''
LeetCode 152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find the contiguous subarray within an
array (containing at least one number) which has the largest product.

Examples:
1. [2,3,-2,4] -> 6
    Explanation: [2,3] has the largest product 6.

2: [-2,0,-1] -> 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray
'''


def max_product(nums: list) -> int:
    '''Time complexity: ~N, Space complexity: ~1'''

    if not nums:
        return 0

    max_so_far = curr_min = curr_max = nums[0]

    for num in nums[1:]:
        choices = num, curr_min * num, curr_max * num
        curr_min = min(choices)
        curr_max = max(choices)

        max_so_far = max(max_so_far, curr_max)

    return max_so_far


assert max_product([2, 3, -2, 4]) == 6
assert max_product([-2, 0, -1]) == 0
