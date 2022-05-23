'''
105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Solution:
Credit: https://bit.ly/3GcK0UV
Credit: https://bit.ly/3lAN6IV

Given preorder and inorder traversal of a tree, construct the binary tree.
For example, given
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder or not inorder:
            return None

        ele = preorder.pop(0)
        root = TreeNode(ele)
        idx = inorder.index(ele)

        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx+1:])

        return root
