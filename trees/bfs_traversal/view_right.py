'''
199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/
Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example:
Input: [1, 2, 3, null, 5, null, 4]
Output: [1, 3, 4]

Explanation:
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''


class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        res, q = [root.val], [root]

        while q:
            next_level = []

            for node in q:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if next_level:
                last_item = next_level[-1].val
                res.append(last_item)

            q = next_level

        return res


class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        res, queue = [], [root]

        while queue:
            size, val = len(queue), 0

            for _ in range(size):
                node = queue.pop(0)
                val = node.val  # store last value in each level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(val)

        return res


class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        ans = [root.val]

        left = ans + self.rightSideView(root.left)
        right = ans + self.rightSideView(root.right)

        if len(right) >= len(left):
            return right

        return right + left[len(right):]
