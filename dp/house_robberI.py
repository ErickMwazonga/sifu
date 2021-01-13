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
    '''Time Complexity: O(n), Space Complexity: O(n)'''

    n = len(nums)
    if n <= 2:
        return max(nums)

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        # The max if we select it or not
        include = nums[i] + dp[i-2]
        exclude = dp[i-1]
        dp[i] = max(include, exclude)

    return dp[-1]

assert rob([1, 2, 3, 1]) == 4
assert rob([2, 7, 9, 3, 1]) == 12
