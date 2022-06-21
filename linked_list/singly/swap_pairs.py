'''
24. Swap Nodes in Pairs
Link: https://leetcode.com/problems/swap-nodes-in-pairs/

Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example:
1. [1, 2, 3, 4] -> [2, 1, 4, 3]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    curr = dummy = ListNode(0, head)

    while curr.next and curr.next.next:
        first = curr.next
        second = curr.next.next

        next_pair = curr.next.next.next

        first.next = next_pair
        second.next = first
        curr.next = second

        curr = curr.next.next

    return dummy.next


def swapPairs_v2(head: ListNode) -> ListNode:
    dummy = ListNode(0, head)
    curr = dummy

    while curr.next and curr.next.next:
        first = curr.next
        second = curr.next.next

        first.next = second.next
        second.next = first
        curr.next = second

        curr = curr.next.next

    return dummy.next
