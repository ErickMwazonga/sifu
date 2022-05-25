'''
1161. Maximum Level Sum of a Binary Tree
Link: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example 1:
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
'''


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return []

        levels = self.levelOrder(root)
        max_sum = float('-inf')
        max_level = 1

        for i in range(len(levels)):
            curr_sum = sum(levels[i])

            if curr_sum > max_sum:
                max_sum = curr_sum
                max_level = i + 1

        return max_level

    def levelOrder(self, root: TreeNode):
        queue, res = [root], []

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(0, level_size):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            res.append(level)

        return res


class Solution2:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = 0
        max_level, max_sum = 0, float('-inf')

        q = [root]

        while q:
            level += 1
            curr_sum = 0

            for _ in range(len(q)):
                node = q.pop(0)

                curr_sum += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if max_sum < curr_sum:
                max_sum = curr_sum
                max_level = level

        return max_level
