'''
Full Binary Tree
A full Binary tree is a special type of binary tree in
which every parent node/internal node has either two or no children.
'''


class Node:

    def __init__(self, item):
        self.item = item
        self.leftChild = None
        self.rightChild = None


def isFullTree(root):

    # Tree empty case
    if not root:
        return True

    # Checking whether child is present
    if not root.leftChild and not root.rightChild:
        return True

    if root.leftChild and root.rightChild:
        return isFullTree(root.leftChild) and isFullTree(root.rightChild)

    return False


root = Node(1)
root.rightChild = Node(3)
root.leftChild = Node(2)

root.leftChild.leftChild = Node(4)
root.leftChild.rightChild = Node(5)
root.leftChild.leftChild.leftChild = Node(6)
root.leftChild.leftChild.rightChild = Node(7)

assert isFullTree(root) == True
