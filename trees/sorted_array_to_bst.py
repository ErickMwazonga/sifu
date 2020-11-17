'''
LeetCode 108. Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of
the two subtrees of every node never differ by more than 1.

Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    Time complexity: O(N).
    Space complexity: O(N).
    '''

    def sortedArrayToBST(self, nums):
        return self.conversion_helper(nums)

    def conversion_helper(self, nums):
        if not nums:
            return None

        n = len(nums)
        if n == 1:
            return TreeNode(nums[0])

        mid = n // 2
        root = TreeNode(nums[mid])

        root.left = self.conversion_helper(nums[0: mid])
        root.right = self.conversion_helper(nums[mid + 1: n])

        return root

    