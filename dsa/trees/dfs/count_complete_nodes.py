'''
222. Count Complete Tree Nodes
https://leetcode.com/problems/count-complete-tree-nodes/

Given the root of a complete binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

Examples:
1. [1, 2, 3, 4, 5, 6] -> 6
2. [] -> 0
3. [1] -> 1
'''


class Solution:
    def countNodes(self, root) -> int:
        if not root:
            return 0

        left = self.countNodes(root.left)
        right = self.countNodes(root.right)

        return 1 + left + right


class Solution_v2:
    def countNodes(self, root) -> int:
        count = [0]  # pass by reference
        self.dfs(root, count)
        return count[0]

    def dfs(self, root, count):
        if not root:
            return

        count[0] += 1

        self.dfs(root.left, count)
        self.dfs(root.right, count)


class Solution_V3:

    def countNodes(self, root):
        left_depth = self.find_left_depth(root)
        right_depth = self.find_right_depth(root)

        if left_depth == right_depth:
            return 2 ** left_depth - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def find_left_depth(self, root):
        if not root:
            return 0

        return self.find_left_depth(root.left) + 1

    def find_right_depth(self, root):
        if not root:
            return 0

        return self.find_right_depth(root.right) + 1
