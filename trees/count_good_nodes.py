'''
1448. Count Good Nodes in Binary Tree
https://leetcode.com/problems/count-good-nodes-in-binary-tree/

Given a binary tree root, a node X in the tree is named good if in the path from root
to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
'''


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root)

    def dfs(self, root, max_node=float('-inf')):
        if not root:
            return 0
        else:
            is_good = root.val >= max_node
            left = self.dfs(root.left, max(max_node, root.val))
            right = self.dfs(root.right, max(max_node, root.val))
            return is_good + left + right
