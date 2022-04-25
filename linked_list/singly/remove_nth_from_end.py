'''
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n: int):
    count, curr = 0, head
    while curr:
        count += 1
        curr = curr.next

    dummy = ListNode(0, head)
    prev, curr = dummy, head
    for _ in range(count - n):
        prev, curr = curr, curr.next

    prev.next = curr.next
    return dummy.next


def removeNthFromEnd_v2(head, n):
    dummy = ListNode(0, head)
    left, right = dummy, head

    while n > 0:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next

    return dummy.next
