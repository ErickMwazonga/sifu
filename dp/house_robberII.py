'''
House Robber II
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

Exampls
Input: [2,3,2] -> 3
Explanation:
You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
because they are adjacent houses.

Input: [1,2,3,1] -> 4
Explanation:
Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
'''


class Solution:
    # Time:  O(n)
    # Space: O(1)

    def rob(self, nums):
        if len(nums) <= 2:
            return max(nums)

        # Max(Not robbing th first house vs
        # Robbing the first house)
        return max(
            self.rob_section(nums[1:]),
            self.rob_section(nums[:-1])
        )

    def rob_section(self, nums):
        n = len(nums)
        money = [0] * n
        money[0] = nums[0]
        money[1] = max(nums[0], nums[1])

        for i in range(2, n):
            money[i] = max(money[i-1], money[i-2] + nums[i])
        return money[-1]


soln = Solution()
assert soln.rob([1, 2, 3, 1]) == 4
assert soln.rob([2, 3, 2]) == 3
