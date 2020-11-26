'''
107. Binary Tree Level Order Traversal II
Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

output -> [15, 7, 9, 20, 3]
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''

def reverse_levelorder_print(self, root):
    if not root:
        return 

    queue, stack = [root], []
    res = []
    
    while queue:
        node = queue.pop(0)
        stack.push(node)

        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    
    while stack:
        node = stack.pop()
        res.append(node.value)

    return res