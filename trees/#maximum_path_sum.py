'''
124. Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes
in the sequence has an edge connecting them. A node can only appear
in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any path.
'''

class Tree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def dfs(root, globalMaxSum):
        if not root:
            return float("-inf")
        else:
            left = dfs(root.left, globalMaxSum)
            right = dfs(root.right, globalMaxSum)

            maxFromTop = max(root.data, root.data+left, root.data+right)
            maxNoTop = max(maxFromTop, root.data+left+right)

            globalMaxSum[0] = max(globalMaxSum[0], maxNoTop)

            return maxFromTop

    def maxPathSum(root):
        globalMaxSum = [float("-inf")] # Pass by reference
        dfs(root, globalMaxSum)
        return globalMaxSum[0]