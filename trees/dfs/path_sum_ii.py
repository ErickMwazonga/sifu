'''
113. Path Sum II
https://leetcode.com/problems/path-sum-ii/

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the 
node values in the path equals targetSum.Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2], [5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
Input: root = [1, 2, 3], targetSum = 5
Output: []
'''


class Solution:
    def pathSum(self, root, targetSum):
        res = []
        self.dfs(root, targetSum, [], res)
        return res

    def dfs(self, root, target, path, res):
        if not root:
            return

        if not root.left and not root.right and target == root.val:
            path.append(root.val)
            res.append(path)
            return

        self.dfs(root.left, target-root.val, path+[root.val], res)
        self.dfs(root.right, target-root.val, path+[root.val], res)


class Solution_V1:
    def pathSum(self, root, targetSum):
        res = []
        self.dfs(root, targetSum, 0, [])
        return res

    def dfs(self, root, res, target, curr_sum, my_list):
        if not root:
            return

        curr_sum += root.val
        my_list.append(root.val)

        if not root.left and not root.right and curr_sum == root.val:
            res.append(my_list[:])

        self.dfs(root.left, res, target, curr_sum, my_list)
        self.dfs(root.right, res, target, curr_sum, my_list)
        my_list.pop()


class Solution_V2:
    def pathSum5(self, root, s):
        if not root:
            return []

        res = []
        stack = [(root, [root.val])]
        while stack:
            curr, ls = stack.pop()
            if not curr.left and not curr.right and sum(ls) == s:
                res.append(ls)

            if curr.right:
                stack.append((curr.right, ls+[curr.right.val]))

            if curr.left:
                stack.append((curr.left, ls+[curr.left.val]))

        return res
