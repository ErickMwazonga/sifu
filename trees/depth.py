
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


def maxDepth(root):
    '''time: 0(n), memory: o(1)'''

    if not root:
        return 0

    depth_left = maxDepth(root.left)
    depth_right = maxDepth(root.right)

    depth = max(depth_left, depth_right) + 1
    return depth


def minDepth(root):
    '''time: 0(n), memory: o(1)'''

    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    # Current node has only right subtree.
    if not root.left:
        return minDepth(root.right) + 1

    # Current node has only left subtree.
    if not root.right:
        return minDepth(root.left) + 1

    depth_left = minDepth(root.left)
    depth_right = minDepth(root.right)

    depth = min(depth_left, depth_right) + 1
    return depth
