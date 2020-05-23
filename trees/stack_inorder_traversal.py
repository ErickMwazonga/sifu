def inorderTraversal(self, root):
    if not root:
        return []

    res = []
    stack = []

    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        res.append(root.val)
        root = root.right

    return res
