'''
114. Flatten Binary Tree to Linked List
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Given a binary tree root, flatten it to a linked list in-place by following the preorder traversal.
For example, given the following tree:
    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''


def flatten(root) -> None:
    '''Do not return anything, modify root in-place instead.'''

    if not root:
        return
    else:
        flatten(root.left)
        flatten(root.right)

        # Store the right subtree
        right_subtree = root.right

        # Reassign the right to the left
        root.right = root.left
        root.left = None

        # Iterate till extreme right
        temp = root
        while temp.right:
            temp = temp.right

        # Join the prev right subtree
        temp.right = right_subtree
