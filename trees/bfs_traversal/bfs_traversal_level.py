'''
LeetCode 102. Binary Tree Level Order Traversal
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

Given a binary tree, return the level order traversal of
its nodes' values. (ie, from left to right, level by level).

Conduct a breadth-first search for level order traversal

Given binary tree [3, 9, 20, null, null, 15, 7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
    [3],
    [9, 20],
    [15, 7]
]
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrder(root: TreeNode):
    '''
    Time complexity: O(N) since each node is processed exactly once.
    Space complexity: O(N) to keep the output structure that contains N node values.
    '''

    if not root:
        return []

    queue, res = [root], []

    while queue:
        level_size = len(queue)
        level = []

        for i in range(0, level_size):
            node = queue.pop(0)
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        res.append(level)

    return res
