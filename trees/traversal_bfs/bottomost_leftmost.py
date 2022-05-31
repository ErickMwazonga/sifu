'''
513. Find Bottom Left Tree Value
Link: https://leetcode.com/problems/find-bottom-left-tree-value/

Given the root of a binary tree, return the leftmost value in the last row of the tree.
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return 0

        levels = self.levelOrder(root)
        return levels[-1][0]

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
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if root is None:
            return []

        queue, result = [root], []

        while queue:
            level, next_queue = [], []

            for root in queue:
                level.append(root.val)

                if root.left:
                    next_queue.append(root.left)

                if root.right:
                    next_queue.append(root.right)

            result.append(level)
            queue = next_queue

        return result[-1][0]
