'''
515. Find Largest Value in Each Tree Row
https://leetcode.com/problems/find-largest-value-in-each-tree-row/

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example 1:
Input: root = [1,3,2,5,3,null,9] -> [1,3,9]

Example 2:
Input: root = [1,2,3] -> [1,3]
'''


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []

        levels = self.levelOrder(root)
        for level in levels:
            max_item = max(level)
            res.append(max_item)

        return res

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

        res, level = [], [root]

        while level:
            new_level = []
            max_node = float('-inf')

            for node in level:
                if node.val > max_node:
                    max_node = node.val

                if node.left:
                    new_level.append(node.left)

                if node.right:
                    new_level.append(node.right)

            res.append(max_node)
            level = new_level

        return res
