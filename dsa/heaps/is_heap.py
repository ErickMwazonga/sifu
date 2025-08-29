'''
Check if a binary tree is a min-heap or not
https://www.techiedelight.com/check-binary-tree-is-min-heap/

Given a binary tree, check if it is a min-heap or not. 
In order words, the binary tree must be a complete binary tree where each node has a higher value than its parent’s value.
'''


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def size(root):
    if not root:
        return 0

    return 1 + size(root.left) + size(root.right)


def isMinHeap(root, i, n):
    if not root:
        return True

    # complete binary tree: out of valid index range
    if i >= n:
        return False

    # Heap property
    not_left = root.left and root.left.data >= root.data
    not_right = root.right and root.right.data <= root.data
    if not_left or not_right:
        return False

    # check for left and right subtree
    check_left = isMinHeap(root.left, 2 * i + 1, n)
    check_right = isMinHeap(root.left, 2 * i + 2, n)

    return check_left and check_right


def isHeap(root):
    return isMinHeap(root, i=0, n=size(root))
