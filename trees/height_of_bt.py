# Write a Program to Find the Maximum Depth or Height of a Tree
# Given a binary tree, find height of it. Height of empty tree is 0

class Node:
    def __init__(self,info): 
        self.info = info  
        self.left = None  
        self.right = None 
    
def height(root):
    if root is None:
        return 0
    
    leftHeight = height(root.left)
    rightHeight = height(root.right)

    # Use the larger one 
    if (leftHeight > rightHeight): 
        return leftHeight + 1
    else: 
        return rightHeight + 1
    
    # return max(leftHeight, rightHeight) + 1

# Driver program to test above function 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
  
  
print ("Height of tree is %d" %(height(root))) 