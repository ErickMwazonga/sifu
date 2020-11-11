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

def preorder_ITERATIVELY(root):
    if not root:
        return []

    res, stack = [], [root]
    while stack:
        node = stack.pop()
        res.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
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

def inorder_ITERATIVELY(root):
    if not root:
        return []

    res, stack = [], []
    while True:
        # push left child if available
        while root:
            stack.append(root)
            root = root.left
        
        if not stack:
            return res

        # retrieve top node and point it to its right child if exists
        node = stack.pop()
        res.append(node.data)
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

def postorder_ITERATIVELY(root):
    if not root:
        return []

    res, stack = [], [root]
    while stack:
        node = stack.pop()
        res.append(node.val)

        # pre-order, right first
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    # reverse result
    return res[::-1]



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
