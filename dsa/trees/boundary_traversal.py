'''
Boundary Traversal of binary tree

The left boundary is defined as the path from the root to the left-most node.
The right boundary is defined as the path from the root to the right-most node.
If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary.
Note this definition only applies to the input binary tree, and not apply to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the
left subtree if it exists. If not, travel to the right subtree. Repeat until you reach a leaf node.
The right-most node is also defined in the same way with left and right exchanged.
For example, boundary traversal of the following tree is “20 8 4 10 14 25 22”
'''


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getLeaves(root, result):
    if root:
        getLeaves(root.left)

        if not root.left and not root.right:
            result.append(root.data)

        getLeaves(root.right)


def getBoundaryLeft(root, result):
    if root:
        if root.left:
            result.append(root.data)
            getBoundaryLeft(root.left)
        elif root.right:
            result.append(root.data)
            getBoundaryLeft(root.right)


def getBoundaryRight(root, result):
    if root:
        if root.right:
            getBoundaryRight(root.right)
            result.append(root.data)
        elif root.left:
            getBoundaryRight(root.left)
            result.append(root.data)


def printBoundary(root):
    result = []

    if root:
        result.append(root.data)
        getBoundaryLeft(root.left, result)
        getBoundaryLeft(root, result)
        getBoundaryRight(root.right, result)

    return result


# Driver program to test above function
root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
printBoundary(root)


# COMPLETE BINARY TREE
# Function to print the nodes of a complete
# binary tree in boundary traversal order
def boundaryTraversal(root):
    # If there is only 1 node print it and return
    if root:
        if not root.left and not root.right:
            print(root.data)
            return

        # List to store order of traversed nodes
        list = []
        list.append(root)

        # Traverse left boundary without root
        # and last node
        temp = root.left
        while temp.left:
            list.append(temp)
            temp = temp.left

        # BFS designed to only include leaf nodes
        q = deque()
        q.append(root)
        while len(q) != 0:
            x = q.pop()
            if not x.left and not x.right:
                list.append(x)
            if x.right:
                q.append(x.right)
            if x.left:
                q.append(x.left)

        # Traverse right boundary without root
        # and last node
        list_r = []
        temp = root.right
        while temp.right:
            list.append(temp)
            temp = temp.right

        # Reversing the order
        list_r = list_r[::-1]

        # Concatenating the two lists
        list += list_r

        # Printing the node's data from the list
        print(" ".join([str(i.data) for i in list]))
    return
