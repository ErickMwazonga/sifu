'''
Convert a Binary Search Tree into a Min Heap
https://www.techiedelight.com/convert-binary-search-tree-into-min-heap/

Given a binary search tree (BST), efficiently convert it into a min-heap. 
In order words, convert a binary search tree into a complete binary tree where each node has a higher value than its parent’s value.
'''


from collections import deque


class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def inorder(root, keys):
    if root is None:
        return

    inorder(root.left, keys)
    keys.append(root.key)
    inorder(root.right, keys)


def preorder(root, keys):
    if root is None:
        return

    root.key = keys.popleft()
    preorder(root.left, keys)
    preorder(root.right, keys)


def convert(root):
    keys = deque()
    inorder(root, keys)
    preorder(root, keys)
