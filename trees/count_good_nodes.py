'''
1448. Count Good Nodes in Binary Tree
https://leetcode.com/problems/count-good-nodes-in-binary-tree/

Given a binary tree root, a node X in the tree is named good if in the path from root
to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
'''


class Solution:
    def goodNodes(self, root) -> int:
        return self.dfs(root)

    def dfs(self, root, max_val=float('-inf')):
        if not root:
            return 0

        is_good = 1 if root.val >= max_val else 0
        curr_max = max(max_val, root.val)

        left = self.dfs(root.left, curr_max)
        right = self.dfs(root.right, curr_max)

        return is_good + left + right
