'''
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Examples:
1. [2, 1, 3] -> True
2. [5, 1, 4, null, null, 3, 6] -> False
Explanation: The root node's value is 5 but its right child's value is 4.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, root, minVal, maxVal):
        if not root:
            return True

        if root.val <= minVal or root.val >= maxVal:
            return False

        left = self.helper(root.left, minVal, root.val)
        right = self.helper(root.right, root.val, maxVal)

        return left and right


class Solution_v2:
    def isValidBST(self, root: TreeNode) -> bool:
        output = []
        self.inOrder(root, output)

        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False

        return True

    def inOrder(self, root, output):
        if not root:
            return

        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)
