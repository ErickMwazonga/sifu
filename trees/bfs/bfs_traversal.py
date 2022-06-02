class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelorder_print(root: TreeNode):
    if not root:
        return

    queue, res = [root], []

    while queue:
        node = queue.pop(0)
        res.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return res


def levelorder_print_v2(self, root):
    if root is None:
        return

    queue, res = [root], []
    i = 0

    while i < len(queue):
        node = queue[i]
        i += 1

        res.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return res
