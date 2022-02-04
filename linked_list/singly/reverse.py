'''
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.
'''


def reverse(head):
    '''Time-O(n), Space-O(1)'''

    prev, curr = None, head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


def reverse_recursive(head):
    '''Time-O(n), Space-O(n)'''

    if not head or not head.next:
        return head

    p = reverse_recursive(head.next)
    head.next.next = head
    head.next = None

    return p
