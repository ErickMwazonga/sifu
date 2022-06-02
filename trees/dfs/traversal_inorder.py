''' 
94. Binary Tree Inorder Traversal
Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
Resource: https://leetcode.com/discuss/study-guide/1072548/A-Beginners-guid-to-BFS-and-DFS

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Examples:
1. [1, null, 2, 3] -> [1, 3, 2]
2. [] -> []
'''


class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


class Inorder:
    '''Time: O(n), Space: O(h)'''

    def inorder(self, root):
        '''Left, Root, Right'''

        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if not root:
            return

        self.dfs(root.left)
        res.append(root.val)
        self.dfs(root.right)


def inorder_ITERATIVELY(root):
    if not root:
        return []

    res, stack = [], []

    while True:
        # push left child if available
        if root:
            stack.append(root)
            root = root.left
        else:
            if not stack:
                return res

            # retrieve top node and point it to its right child if exists
            node = stack.pop()
            res.append(node.val)
            root = node.right

    return res
