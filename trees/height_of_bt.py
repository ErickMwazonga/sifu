# Write a Program to Find the Maximum Depth or Height of a Tree
# Given a binary tree, find height of it. Height of empty tree is 0


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


def height(root):
    '''
    time: 0(n)
    memory: o(1)
    '''

    if root is None:
        return 0

    leftHeight = height(root.left)
    rightHeight = height(root.right)

    depth = max(depth_left, depth_right) + 1
    return depth

def maximumDepth(root):
    '''
    time: 0(n), memory: o(1)
    '''

    if root is None:
        return 0

    leftHeight = maximumDepth(root.left)
    rightHeight = maximumDepth(root.right)

    depth = max(depth_left, depth_right) + 1
    return depth


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print ("Height of tree is %d" %(height(root)))