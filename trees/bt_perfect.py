'''
Perfect Binary Tree
A perfect binary tree is a type of binary tree in which
every internal node has exactly two child nodes and all
the leaf nodes are at the same level.

# NB
All the internal nodes have a degree of 2.
'''


class Node:
    def __init__(self, k):
        self.key = k
        self.right = self.left = None


# Calculate the depth
def calculateDepth(node):
    d = 0
    while node:
        d += 1
        node = node.left
    return d


# Check if the tree is perfect binary tree
def is_perfect(root, d, level=0):
    # An empty tree is perfect
    if not root:
        return True

    if not root.left or not root.right:
        return False

    # If leaf node, then its depth must
    # be same as depth of all other leaves.
    if not root.left and not root.right:
        return d == level + 1

    left_is_perfect = is_perfect(root.left, d, level + 1)
    right_is_perfect = is_perfect(root.right, d, level + 1)

    return left_is_perfect and right_is_perfect


def main(root):
    is_perfect(root, calculateDepth(root))
