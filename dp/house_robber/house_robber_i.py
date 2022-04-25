'''
198. House Robber
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them
is that adjacent houses have security system connected and 
it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given a list of non-negative integers representing the
amount of money of each house, determine the maximum amount
of money you can rob tonight without alerting the police.

Input: [1, 2, 3, 1]
Output: 4 -> 1 + 3 = 4.

Input: [2, 7, 9, 3, 1]
Output: 12 -> 2 + 9 + 1 = 12.
'''


def rob(nums):
    for i in range(1, len(nums)):
        if i == 1:
            nums[i] = max(nums[i], nums[i-1])
        else:
            rob = nums[i] + nums[i-2]
            dont_rob = nums[i-1]
            nums[i] = max(rob, dont_rob)

    return nums[-1]


def rob_v2(nums: list[int]) -> int:
    '''Time: O(n), Space: O(n)'''

    if not nums:
        return 0

    n = len(nums)
    if n <= 2:
        return max(nums)

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        # The max if we rob it or not
        rob = nums[i] + dp[i-2]
        dont_rob = dp[i-1]
        dp[i] = max(rob, dont_rob)

    return dp[-1]


assert rob([1, 2, 3, 1]) == 4
assert rob([2, 7, 9, 3, 1]) == 12


def rob_v3(nums):
    rob, not_rob = 0, 0

    for num in nums:
        rob, not_rob = not_rob + num, max(rob, not_rob)

    return max(rob, not_rob)
