''' 
145. Binary Tree Postorder Traversal
Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
Resource: https://leetcode.com/discuss/study-guide/1072548/A-Beginners-guid-to-BFS-and-DFS

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Examples:
1. [1, null, 2, 3] -> [3, 2, 1]
2. [] -> []
3. [1] -> [1]
'''


class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


class PostOrder:
    '''Time: O(n), Space: O(h)'''

    def postorder(self, root):
        '''Left, Right, Root'''

        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if not root:
            return

        self.dfs(root.left)
        self.dfs(root.right)
        res.append(root.val)


def postorder_ITERATIVELY(root):
    if not root:
        return []

    res, stack = [], [root]
    while stack:
        node = stack.pop()
        res.append(node.val)

        # pre-order, right first
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    # reverse result
    return res[::-1]
