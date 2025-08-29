''' 
144. Binary Tree Preorder Traversal
Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
Resource: https://leetcode.com/discuss/study-guide/1072548/A-Beginners-guid-to-BFS-and-DFS

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Examples:
1. [1, null, 2, 3] -> [1, 2, 3]
2. [] -> []
3. [1] -> [1]
'''


class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


class Preorder:
    '''Time: O(n), Space: O(h)'''

    def preorder(self, root):
        '''Root, Left, Right'''

        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if not root:
            return

        res.append(root.val)
        self.dfs(root.left)
        self.dfs(root.right)


def preorder_ITERATIVELY(root):
    if not root:
        return []

    res, stack = [], [root]
    while stack:
        node = stack.pop()
        res.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return res
