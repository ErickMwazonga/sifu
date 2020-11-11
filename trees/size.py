'''
The "size" of a binary tree is the total number of nodes present in the binary tree.
We will explicitly define this quantity in greater detail and cover a strategy for
how one may calculate this quantity in the binary tree data structure
we have been building in this series of videos.
'''

def size_(self, node):
    if not node:
        return 0
    return 1 + self.size_(node.left) + self.size_(node.right)

def size(self):
    if self.root is None:
        return 0

    stack = Stack()
    stack.push(self.root)

    size = 1
    while stack:
        node = stack.pop()
        if node.left:
            size += 1
            stack.push(node.left)
        if node.right:
            size += 1
            stack.push(node.right)

    return size