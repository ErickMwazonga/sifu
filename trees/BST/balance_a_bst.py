'''
1382. Balance a Binary Search Tree
Link: https://leetcode.com/problems/balance-a-binary-search-tree/

Given a binary search tree, return a balanced binary search tree with the same node values.
A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.
If there is more than one answer, return any of them.

Example:
Input: root = [1, null, 2, null, 3, null, 4, null, null]
Output: [2, 1, 3, null, null, null, 4]
Explanation: This is not the only correct answer,  [3, 1, 4, null, 2, null, null] is also correct.
'''


class TreeNode:
    pass


def balanceBST(root):
    inorder_array = []

    # build inorder traversal of the BST
    def buildArray(node):
        if not node:
            return

        buildArray(node.left)
        inorder_array.append(node.val)
        buildArray(node.right)

    # build a BST from inorder array
    def balanceBSTHelper(inorder_array):
        if not inorder_array:
            return

        mid = len(inorder_array) // 2
        node = TreeNode(inorder_array[mid])
        node.left = balanceBSTHelper(inorder_array[:mid])
        node.right = balanceBSTHelper(inorder_array[mid + 1:])

        return node

    buildArray(root)
    return balanceBSTHelper(inorder_array)
