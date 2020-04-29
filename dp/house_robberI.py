'''
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them
is that adjacent houses have security system connected and 
it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given a list of non-negative integers representing the
amount of money of each house, determine the maximum amount
of money you can rob tonight without alerting the police.

Input: [1,2,3,1]
Output: 4 -> 1 + 3 = 4.

Input: [2,7,9,3,1]
Output: 12 -> 2 + 9 + 1 = 12.
'''

from typing import List

def rob(nums: List[int]) -> int:
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    if not nums:
        return 0

    n = len(nums)
    if n <= 2:
        return max(nums)

    DP = [0] * n
    DP[0] = nums[0]
    DP[1] = max(nums[0], nums[1])

    for i in range(2, n):
        # The max if we select it or not
        DP[i] = max(nums[i] + DP[i-2], DP[i-1])

    return DP[-1]

assert rob([1, 2, 3, 1]) == 4
assert rob([2, 7, 9, 3, 1]) == 12


def rob2(nums: List[int]) -> int:
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    if not nums:
        return 0

    n = len(nums)
    if n <= 2:
        return max(nums)

    pre_list = [0, 0]
    for i in range(n):
        max_value = max(pre_list[0] + nums[i], pre_list[1])
        pre_list[0] = pre_list[1]
        pre_list[1] = max_value

    return pre_list[1]

assert rob2([1, 2, 3, 1]) == 4
assert rob2([2, 7, 9, 3, 1]) == 12
