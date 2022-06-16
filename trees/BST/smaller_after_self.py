'''
315. Count of Smaller Numbers After Self
https://leetcode.com/problems/count-of-smaller-numbers-after-self/

You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example 1:
Input:  [5, 2, 6, 1]
Output: [2, 1, 1, 0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
'''


class Solution:
    def countSmaller(self, nums):
        res = [0] * len(nums)
        bst = BST()

        # Insert into BST and get left count.
        for i in reversed(range(len(nums))):
            bst.insert(nums[i])
            res[i] = bst.query(nums[i])

        return res


class BSTNode(object):
    def __init__(self, val):
        self.val = val
        self.count = 0
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = BSTNode(val)
            return

        curr = self.root
        while curr:
            node = BSTNode(val)

            if node.val < curr.val:  # Insert left if smaller.
                curr.count += 1  # Increase the number of left children.

                if not curr.left:
                    curr.left = node
                    break

                curr = curr.left

            else:  # Insert right if larger or equal.
                if not curr.right:
                    curr.right = node
                    break

                curr = curr.right

    # Query the smaller count of the value.
    def query(self, val):
        count = 0
        curr = self.root

        while curr:
            if curr.val == val:
                return count + curr.count

            if val < curr.val:
                curr = curr.left
            else:
                # Count the number of the smaller nodes.
                count += curr.count + 1
                curr = curr.right

        return count
