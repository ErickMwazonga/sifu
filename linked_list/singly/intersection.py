'''
160. Intersection of Two Linked Lists
Link: https://leetcode.com/problems/intersection-of-two-linked-lists/

Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:
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
    def getLength(self, head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length

    def getIntersectionNode(self, headA, headB):
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)

        # make A to be the longest by swapping
        if lenB > lenA:
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA

        diff = lenA - lenB
        while diff:
            headA = headA.next
            diff -= 1

        while headA != headB:
            headA, headB = headA.next, headB.next

        return headA
