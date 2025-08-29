'''
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along 
the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3, 9, 20, null, null, 15, 7]
Output: 3

Example 2:
Input: root = [1, null, 2]
Output: 2
'''

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


def maxDepth(root):
    '''Time: 0(n), Memory: o(1)'''

    if not root:
        return 0

    depth_left = maxDepth(root.left)
    depth_right = maxDepth(root.right)

    depth = 1 + max(depth_left, depth_right)
    return depth


def minDepth(root):
    '''Time: 0(n), Memory: o(1)'''

    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    # Current node has only right subtree.
    if not root.left:
        return minDepth(root.right) + 1

    # Current node has only left subtree.
    if not root.right:
        return minDepth(root.left) + 1

    depth_left = minDepth(root.left)
    depth_right = minDepth(root.right)

    depth = 1 + min(depth_left, depth_right)
    return depth
