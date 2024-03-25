'''
160. Intersection of Two Linked Lists
Link: https://leetcode.com/problems/intersection-of-two-linked-lists/

Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:

INTUITION
- Iterate the 2 lists with combination of each other until they meet because their lengths will be equal
[4,1,8,4,5] + [5,6,1,8,4,5] -> [4,1,8,4,5,5,6,1,8,4,5] 
[5,6,1,8,4,5] + [4,1,8,4,5] -> [5,6,1,8,4,5,4,1,8,4,5]
[8, 4, 5] >> Will point to the same memory location
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA, headB):
    seen = set()

    while headA:
        seen.add(headA)
        headA = headA.next

    while headB:
        if headB in seen:
            return headB
        headB = headB.next

    return None


def getIntersectionNode(headA, headB):
    '''
    1. https://bit.ly/3sQn7l1
    2. https://www.youtube.com/watch?v=D0X0BONOQhI
    '''

    if not headA or not headB:
        return None

    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA

    return a

class Solution_V3:
    def getIntersectionNode(self, headA, headB):
        lenA = self.length(headA)
        lenB = self.length(headB)
        
        # Find the longer and shorter lists
        longer = headA if lenA > lenB else headB
        shorter = headB if lenA > lenB else headA
        
        # Align the longer list to the same starting point as the shorter list
        for _ in range(abs(lenA - lenB)):
            longer = longer.next
        
        # Iterate through both lists until intersection is found
        while shorter != longer:
            shorter = shorter.next
            longer = longer.next
        
        return shorter

    def length(self, head: ListNode) -> int:
        length, curr = 0, head
        while curr:
            length += 1
            curr = curr.next
        return length
