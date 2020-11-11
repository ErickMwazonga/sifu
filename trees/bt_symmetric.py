'''
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
 
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        return self.isMirror(root.left, root.right)

    def isMirror(self, left_root, right_root):
        if not left_root and not right_root:
            return True
    
        if not left_root or not right_root:
            return False
 
        if left_root.val != right_root.val:
            return False
        
        left_isMirror = self.isMirror(left_root.left, right_root.right)
        right_isMirror = self.isMirror(left_root.right, right_root.left)

        return left_isMirror and right_isMirror