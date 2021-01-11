# Importing dependancies
import sys

"""
To see if a binary tree is a binary search tree, check:
If a node is a left child, then its key and the keys of 
the nodes in its right subtree are less than its parent’s key.
If a node is a right child, then its key and the keys of
the nodes in its left subtree are greater than its parent’s key.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
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


# RECURSIVE SOLUTION
def isBST(root, _min=float('-inf'), _max=float('inf')):
    if not root:
        return True
    elif root.data <= _min or root.data >= _max:
        return False
    else:
        return isBST(root.left, _min, root.data) and
                isBST(root.right, root.data, _max)