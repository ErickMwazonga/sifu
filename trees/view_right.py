class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        
        results, q = [root.val], [root]
        
        while q:
            next_level = []
            for node in q:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if next_level:
                results.append(next_level[-1].val)
            
            q = next_level
        
        return results

class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        res, queue = [], [root]

        while queue:
            size, val = len(queue), 0

            for _ in range(size): 
                node = queue.pop(0)
                val = node.val # store last value in each level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(val)

        return res

class Solution(object):
    def rightSideView(self, root):
        if root==None:
            return []

        ans = [root.val]

        left = ans + self.rightSideView(root.left)
        right = ans + self.rightSideView(root.right)

        if len(right) >= len(left):
            return right

        return right + left[len(right):]


