# Tree traversals
# Traversing a tree means visiting every node in the tree.


class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


def inorder(root):
    '''Left, Root, Right'''

    if root:
        inorder(root.left)
        print(str(root.val) + "->", end='')
        inorder(root.right)


def postorder(root):
    '''Left, Right, Root'''

    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) + "->", end='')


def preorder(root):
    '''Root, Left, Right'''

    if root:
        print(str(root.val) + "->", end='')
        preorder(root.left)
        preorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal ")
inorder(root)  # 4->2->5->1->3->

print("\nPreorder traversal ")
preorder(root)  # 1->2->4->5->3->

print("\nPostorder traversal ")
postorder(root)  # 4->5->2->3->1->
