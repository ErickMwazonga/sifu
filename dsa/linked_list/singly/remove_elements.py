'''
203. Remove Linked List Elements
Link: https://leetcode.com/problems/remove-linked-list-elements/

Given the head of a linked list and an integer val, remove all the nodes of the linked list that 
has Node.val == val, and return the new head.

Example 1:
Input: [1, 2, 6, 3, 4, 5, 6], val = 6
Output: [1, 2, 3, 4, 5]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head, val):
    dummy = ListNode(next=head)
    prev, curr = dummy, head

    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr

        curr = curr.next

    return dummy.next
