'''
226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

Example:
Input:
     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''


class Solution:

    def invertTree(self, root):
        if not root:
            return

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    # DFS
    def invert_tree_2(self, root):
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.right, node.left])

        return root
