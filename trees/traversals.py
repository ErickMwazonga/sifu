# Tree traversals
# Traversing a tree means visiting every node in the tree.


class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item

def preorder(root):
    '''Root, Left, Right'''

    data = []

    def traverse(root):
        if not root:
            return

        data.append(root.data)
        traverse(root.left)
        traverse(root.right)

    traverse(root)
    return data

def preorder_ITERATIVELY(self, root: TreeNode):
    res = []
    stack = []

    if not root:
        return res

    stack.append(root)
    while stack:
        node = stack.pop()
        if node:
            res.append(node.data)
            stack.append(node.right)
            stack.append(node.left)

    return res

def inorder(root):
    '''Left, Root, Right'''

    data = []

    def traverse(root):
        if not root:
            return

        traverse(root.left)
        data.append(root.data)
        traverse(root.right)

    traverse(root)
    return data

def inorder_ITERATIVELY(self, root):
    res = []
    stack = []

    if not root:
        return res

    while True:
        # push left child if available
        while root:
            stack.append(root)
            root = root.left
        
        if not stack:
            return res

        # retrieve top node and point it to its right child if exists
        node = stack.pop()
        res.append(node.val)
        root = node.right
    
    return res


def postorder(root):
    '''Left, Right, Root'''

    data = []

    def traverse(root):
        if not root:
            return

        traverse(root.left)
        traverse(root.right)
        data.append(root.data)

    traverse(root)
    return data


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
