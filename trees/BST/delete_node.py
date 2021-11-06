'''
450. Delete Node in a BST
https://leetcode.com/problems/delete-node-in-a-bst/

Given a root node reference of a BST and a key, delete the node with the given key in the BST.
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:
Search for a node to remove.
If the node is found, delete the node.
'''


class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def getMinNode(root):
    while root.left:
        root = root.left
    return root


def deleteNodeBst(root, num):
    if root is None:
        return None
    elif num < root.data:
        root.left = deleteNodeBst(root.left, num)
    elif num > root.data:
        root.right = deleteNodeBst(root.right, num)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            successor = getMinNode(root.right)
            root.data = successor.data
            root.right = deleteNodeBst(root.right, successor.data)

    return root
