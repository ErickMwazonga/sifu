'''
617. Merge Two Binary Trees
https://leetcode.com/problems/merge-two-binary-trees/

You are given two binary trees root1 and root2.
You need to merge the two trees into a new binary tree.
The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of the new tree.

Example 1:
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Example 2:
Input: root1 = [1], root2 = [1,2]
Output: [2,2]
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    if not t1 and not t2:
        return None

    v1 = t1.val if t1 else 0
    v2 = t2.val if t2 else 0
    root = TreeNode(v1 + v2)

    t1 = t1 if t1 else TreeNode()
    t2 = t2 if t2 else TreeNode()

    root.left = self.mergeTrees(t1.left, t2.left)
    root.right = self.mergeTrees(t1.right, t2.right)

    return root


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 and not root2:
            return None

        val1 = root1.val if root1 else 0
        val2 = root2.val if root2 else 0

        new_tree = TreeNode(val1 + val2)

        new_tree.left = self.mergeTrees(
            root1.left if root1 else None,
            root2.left if root2 else None
        )

        new_tree.right = self.mergeTrees(
            root1.right if root1 else None,
            root2.right if root2 else None
        )

        return new_tree


class Solution2:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1

    def mergeTreesV2(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 and not root2:
            return None

        if root1 and root2:
            new_tree = TreeNode(root1.val + root2.val)

            new_tree.left = self.mergeTrees(root1.left, root2.left)
            new_tree.right = self.mergeTrees(root1.right, root2.right)

            return new_tree
        else:
            return root1 or root2


class Solution3(object):
    def mergeTrees(self, t1, t2):
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)

            return root
        else:
            return t1 or t2
