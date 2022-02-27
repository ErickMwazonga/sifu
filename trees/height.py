# Write a Program to Find the Maximum Depth or Height of a Tree
# Given a binary tree, find height of it. Height of empty tree is 0


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


def height(root):
    '''Time: 0(n), Memory: o(1)'''

    if not root:
        return 0

    leftHeight = height(root.left)
    rightHeight = height(root.right)

    depth = max(leftHeight, rightHeight) + 1
    return depth


def maxDepth(root):
    '''time: 0(n), memory: o(1)'''

    if not root:
        return 0

    depth_left = maxDepth(root.left)
    depth_right = maxDepth(root.right)

    depth = max(depth_left, depth_right) + 1
    return depth


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(f'Height of tree is {(height(root))}')
