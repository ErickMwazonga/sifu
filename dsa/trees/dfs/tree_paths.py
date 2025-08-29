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
        self.dfs(root, '', res)
        return res

    def dfs(self, node, path, res):
        if not node:
            return

        if not node.left and not node.right:
            res.append(f'{path}{node.val}')

        self.dfs(node.left, f'{path}{node.val}->', res)
        self.dfs(node.right, f'{path}{node.val}->', res)


class Solution_V2:
    def binaryTreePaths(self, root):
        if not root:
            return []

        res = []
        self.dfs(root, path='', res=res)
        return res

    def dfs(self, root, path, res):
        path += str(root.val)

        if not root.left and not root.right:
            res.append(path)
            return

        new_str = path + '->'
        if root.left:
            self.dfs(root.left, new_str, res)

        if root.right:
            self.dfs(root.right, new_str, res)


class Solution_V3:
    def binaryTreePaths(self, root):
        if not root:
            return []

        res = []
        stack = [(root, '')]

        while stack:
            node, path = stack.pop()

            if not node:
                continue

            if not node.left and not node.right:
                res.append('{}{}'.format(path, node.val))

            new_path = path + str(node.val) + '->'
            stack.append((node.left, new_path))
            stack.append((node.right, new_path))

        return res


class Solution_V4:
    def binaryTreePaths(self, root):
        if not root:
            return []

        res, stack = [], [(root, '')]

        while stack:
            node, path = stack.pop()

            if not node.left and not node.right:
                res.append(path + str(node.val))

            new_path = path + str(node.val) + '->'
            if node.right:
                stack.append((node.right, new_path))

            if node.left:
                stack.append((node.left, new_path))

        return res
