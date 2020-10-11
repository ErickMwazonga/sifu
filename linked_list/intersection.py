'''
LeetCode 160. Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        visited = set()
        
        while headA != None:            
            visited.add(headA)
            headA = headA.next

        while headB != None:            
            if headB in visited:
                return headB
            headB = headB.next
        
        return None