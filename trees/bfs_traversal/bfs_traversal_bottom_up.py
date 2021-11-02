'''
107. Binary Tree Level Order Traversal II
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''


def levelOrderBottom(root: TreeNode):
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

        res.insert(0, level)

    return res
