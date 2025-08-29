'''
515. Find Largest Value in Each Tree Row
Link: https://leetcode.com/problems/find-largest-value-in-each-tree-row/

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Examples:
1. [1, 3, 2, 5, 3, null, 9] -> [1, 3, 9]
2. [1, 2, 3] -> [1, 3]
'''


import queue


class TreeNode:
    pass


class Solution:
    def largestValues(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        levels = self.levelOrder(root)
        return [max(level) for level in levels]

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
    def largestValues(self, root):
        if not root:
            return []

        res, queue = [], [root]

        while queue:
            level = []
            max_node = float('-inf')

            for node in queue:
                max_node = max(max_node, node.val)

                if node.left:
                    level.append(node.left)

                if node.right:
                    level.append(node.right)

            res.append(max_node)
            queue = level

        return res
