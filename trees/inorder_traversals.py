class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
        result = []
        self.traverse(root, result)
        return result
        
    def traverse(self, root, result):
        if not root:
            return

        self.traverse(root.left, result)
        result.append(root.val)
        self.traverse(root.right, result)

    def ITERATIVELY(self, root):
        res = []
        stack = []

        if not root:
            return res

        while True:
            while root:
                stack.append(root)
                root = root.left
            
            if not stack:
                return res

            node = stack.pop()
            res.append(node.val)
            root = node.right
          