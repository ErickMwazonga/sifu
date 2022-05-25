'''
257. Binary Tree Paths
Link: https://leetcode.com/problems/binary-tree-paths/

Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.

Example:
Input:
   1
 /   \
2     3
 \
  5

Output: ['1->2->5', '1->3']
Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''


class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []

        res = []
        self.path(root, '', res)
        return res

    def path(self, root, string, res):
        string += str(root.val)

        if not root.left and not root.right:
            res.append(string)

        if root.left:
            new_str = string + '->'
            self.path(root.left, new_str, res)

        if root.right:
            new_str = string + '->'
            self.path(root.right, new_str, res)
