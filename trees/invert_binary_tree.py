'''
226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

Example:
Input:
     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

import collections


def invertTree(self, root: TreeNode) -> TreeNode:
    if not root:
        return

    root.left, root.right = root.right, root.left
    self.invertTree(root.left)
    self.invertTree(root.right)

    return root

# BFS


def invertTree2(self, root):
    queue = collections.deque([(root)])
    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
    return root

# DFS


def invertTree(self, root):
    stack = [root]

    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack.extend([node.right, node.left])

    return root
