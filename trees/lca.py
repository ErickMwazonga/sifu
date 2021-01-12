'''
236. Lowest Common Ancestor of a Binary Tree
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
two nodes p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of
itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
'''

def lowestCommonAncestor(self, root, p, q):
    '''Time complexity: O(n), Space complexity: O(h)'''

    if not root:
        return None

    # found p and q?
    if root == p or root == q:
        return root

    # search left and right subtree
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)

    # p and q appears in left and right respectively, then their ancestor is root
    if left and right:
        return root
    
    # p and q not in left, then it must be in right, otherwise left
    return left or right
