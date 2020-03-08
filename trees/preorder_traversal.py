'''
https://leetcode.com/problems/binary-tree-preorder-traversal/
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [1,2,3]
'''

def preorderTraversal(self, root):
    '''Iteratively'''
    if not root:
        return []
    
    res = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        
        if node:
            res.append(node.val)
            
            stack.append(node.right)
            stack.append(node.left)
        
    return res