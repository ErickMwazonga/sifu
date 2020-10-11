class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.traverse(root, result)
        return result
    
    def traverse(self, root, result):
        if not root:
            return 
        
        result.append(root.val)
        self.traverse(root.left, result)
        self.traverse(root.right, result) 

    def ITERATIVELY(self, root: TreeNode) -> List[int]:
        res = []
        stack = []

        if not root:
            return res

        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)

        return res