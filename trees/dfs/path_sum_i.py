'''
112. Path Sum
https://leetcode.com/problems/path-sum/

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path 
such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
'''


class Solution:
    def hasPathSum(self, root, targetSum):
        return self.dfs(root, targetSum, curSum=0)

    def dfs(self, root, targetSum, curSum):
        if not root:
            return False

        curSum += root.val

        if not root.left and not root.right:
            return curSum == targetSum

        has_left = self.dfs(root.left, targetSum, curSum)
        has_right = self.dfs(root.right, targetSum, curSum)

        return has_left or has_right


class Solution_V2:

    def hasPathSum(self, root, target):
        if not root:
            return False

        if not root.left and not root.right and root.val == target:
            return True

        has_left = self.hasPathSum(root.left, target - root.val)
        has_right = self.hasPathSum(root.right, target - root.val)

        return has_left or has_right


class Solution_V3:

    def hasPathSum(self, root, sum):
        if not root:
            return False

        stack = [(root, sum)]
        while stack:
            node, _sum = stack.pop()

            if not node.left and not node.right and node.val == _sum:
                return True

            if node.left:
                stack.append((node.left, _sum - node.val))
            if node.right:
                stack.append((node.right, _sum - node.val))

        return False
