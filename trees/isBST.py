# Importing dependancies
import sys

"""
To see if a binary tree is a binary search tree, check:
If a node is a left child, then its key and the keys of 
the nodes in its right subtree are less than its parent’s key.
If a node is a right child, then its key and the keys of
the nodes in its left subtree are greater than its parent’s key.
"""


class Tree: 
  def __init__(self, data): 
    self.data = data 
    self.left = None
    self.right = None

# A function to check if a binary tree is BST.
def isBST(node, mini, maxi):
  # Base case. An empty tree is a BST.
  if node == None:
    return 1
  # Checking if a key is outside the permitted range.
  if node.data < mini:
    return 0
  if node.data > maxi:
    return 0
  # Sending in updates ranges to the right and left subtree
  return isBST(node.right, node.data, maxi) and isBST(node.left, mini, node.data) 

# Creating a BST
root = Tree(6) 
root.left = Tree(3) 
root.right = Tree(9) 
root.left.left = Tree(1) 
root.left.right = Tree(5) 
root.right.left = Tree(7)
root.right.right = Tree(11)
# Passing in the word size of the machine
mini = -sys.maxsize - 1
maxi = sys.maxsize
if(isBST(root, mini, maxi)):
  print("This binary tree is a BST.")
else:
  print("This binary tree is not a BST.")
