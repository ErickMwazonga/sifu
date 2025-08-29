class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bfs(root: TreeNode):
    if not root:
        return []

    queue, res = [root], []

    while queue:  # o(n)
        node = queue.pop(0)  # o(n)
        res.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return res


def bfs_v2(root):
    '''Time: O(n), Space: O(n)'''

    if not root:
        return []

    queue, res = [root], []
    i = 0

    while i < len(queue):
        popped = queue[i]
        i += 1

        res.append(popped.val)

        if not popped:
            continue

        queue.append(popped.left)
        queue.append(popped.right)

    return res


class Solution:

    def bfs(self, root):
        res, queue = [], [root]
        self.traverse(root, queue=queue, i=0, res=res)
        return res

    def traverse(self, root, queue, i, res):
        if i >= len(queue):
            return

        popped = queue[i]
        if not popped:
            return

        res.append(popped.val)
        queue.append(root.left)
        queue.append(root.right)

        self.traverse(root, queue, i + 1, res)
