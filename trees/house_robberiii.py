'''
House Robber III
https://leetcode.com/problems/house-robber-iii/
https://www.hrwhisper.me/leetcode-house-robber-iii/
The thief has found himself a new place for his thievery again.
There is only one entrance to this area, called the "root."
Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that "all houses in this place forms a binary tree".
It will automatically contact the police if two directly-linked
houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight
without alerting the police.
'''


# TODO
class Solution(object):
    def rob(self, root):
        return self.dfs_rob(root)[0]

    def dfs_rob(self, root):
        if not root:
            return 0, 0
        rob_L, no_rob_L = self.dfs_rob(root.left)
        rob_R, no_rob_R = self.dfs_rob(root.right)
        return max(no_rob_L + no_rob_R + root.val, rob_L + rob_R), rob_L + rob_R