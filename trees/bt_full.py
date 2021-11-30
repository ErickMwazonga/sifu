'''
Full Binary Tree
A full Binary tree is a special type of binary tree in
which every parent node/internal node has either two or no children.
'''


class Node:

    def __init__(self):
        self.leftChild = None
        self.rightChild = None

    def isFullTree(self, root):
        # Tree empty case
        if not root:
            return True

        # Checking whether child is present
        if not root.leftChild and not root.rightChild:
            return True

        if not root.leftChild or not root.rightChild:
            return False

        return self.isFullTree(root.left) and self.isFullTree(root.right)


root = Node(1)
root.rightChild = Node(3)
root.leftChild = Node(2)

root.leftChild.leftChild = Node(4)
root.leftChild.rightChild = Node(5)
root.leftChild.leftChild.leftChild = Node(6)
root.leftChild.leftChild.rightChild = Node(7)

node = Node()
assert node.isFullTree(root) == True
