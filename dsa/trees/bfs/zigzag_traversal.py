'''
103. Binary Tree Zigzag Level Order Traversal
Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Resource: https://bit.ly/3wC1mYc
Resource: https://bit.ly/3yRjsaa

Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3, 9, 20, null, null, 15, 7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20, 9],
  [15, 7]
]
'''


def zigzagLevelOrder(root: TreeNode):

    if not root:
        return []

    queue, res = [root], []
    even_level = False

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.pop(0)
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if even_level:
            res.append(level[::-1])
        else:
            res.append(level)

        even_level = not even_level

    return res


def zigzagLevelOrder(root: TreeNode):
    if not root:
        return []

    queue, res = [root], []
    even_level = False

    while queue:
        n = len(queue)
        level = [0] * n

        for i in range(n):
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if even_level:
                level[n-1-i] = node.val
            else:
                level[i] = node.val

        res.append(level)
        even_level = not even_level

        return res
