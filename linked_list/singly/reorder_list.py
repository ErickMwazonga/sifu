'''
143. Reorder List
https://leetcode.com/problems/reorder-list/

You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1, 2, 3, 4]
Output: [1, 4, 2, 3]

Example 2:
Input: head = [1, 2, 3, 4, 5]
Output: [1, 5, 2, 4, 3]
'''


def reverse(node):
    curr, prev = node, None

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


def reorderList(head):
    # Find Middle
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    second = reverse(slow.next)
    slow.next = None

    # Merge two halves
    first, second = head, second
    while second:
        nxt = first.next
        first.next = second
        first = second
        second = nxt

    # while second:
    #     next_first, next_sec = first.next, second.next
    #     first.next = second
    #     second.next = next_first
    #     first, second = next_first, next_sec
