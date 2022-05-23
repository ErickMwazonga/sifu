'''
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Resource - https://bit.ly/3z9B55x

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
    ptr, length = head, 0
    while ptr:
        ptr, length = ptr.next, length + 1

    # Deleting first node
    if length == n:
        return head.next

    ptr = head
    for _ in range(1, length - n):
        ptr = ptr.next

    ptr.next = ptr.next.next
    return head


def removeNthFromEnd_v2(head, n: int):
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


def removeNthFromEnd_v3(head, n):
    fast = slow = head
    for _ in range(n):
        fast = fast.next

    if not fast:
        return head.next

    while fast.next:
        fast, slow = fast.next, slow.next

    slow.next = slow.next.next
    return head
