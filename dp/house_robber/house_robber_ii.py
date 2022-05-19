'''
House Robber II
https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have security system connected
and it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given a list of non-negative integers representing the
amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.

Example
Input: [2, 3, 2] -> 3
Explanation:
You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
because they are adjacent houses.
'''


class Solution:
    '''Time:  O(n) # Space: O(n)'''

    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        exclude_first = self.rob_section(nums[1:])
        exclude_last = self.rob_section(nums[:-1])

        return max(exclude_first, exclude_last)

    def rob_section(self, nums):
        rob, no_rob = 0, 0

        for num in nums:
            rob_value = max(rob, no_rob + num)
            no_rob = rob
            rob = rob_value

        return rob


soln = Solution()
assert soln.rob([1, 2, 3, 1]) == 4
assert soln.rob([2, 3, 2]) == 3
