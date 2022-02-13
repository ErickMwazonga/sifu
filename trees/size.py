'''
The size of a binary tree is the total number of nodes present in the binary tree.
We will explicitly define this quantity in greater detail and cover a strategy for
how one may calculate this quantity in the binary tree data structure
we have been building in this series of videos.
'''


def size_(self, node):
    if not node:
        return 0
    return 1 + self.size_(node.left) + self.size_(node.right)


def size(self):
    if not self.root:
        return 0

    stack = [self.root]

    size = 1
    while stack:
        node = stack.pop()
        if node.left:
            stack.push(node.left)
            size += 1
        if node.right:
            stack.push(node.right)
            size += 1

    return size
