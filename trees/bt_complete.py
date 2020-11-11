'''
958. Check Completeness of a Binary Tree
https://leetcode.com/problems/check-completeness-of-a-binary-tree/

Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last,
is completely filled, and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:
Input: [1,2,3,4,5,6] -> true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}),
and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example 2:
Input: [1,2,3,4,5,null,7] -> false
Explanation: The node with value 7 isn't as far left as possible.
'''

class Solution:
    '''
    Use BFS to do a level order traversal, add children to the bfs queue,
    until we met the first empty node. For a complete binary tree,
    there should not be any node after we met an empty one.
    '''
    def isCompleteTree(self, root) -> bool:
        if not root:
            return True

        queue = [root]
        while queue:
            node = queue.pop(0)

            if not node:
                break
            
            queue.append(node.left)
            queue.append(node.right)

        # there should not be any node after we met an empty one
        return not any(queue)
        