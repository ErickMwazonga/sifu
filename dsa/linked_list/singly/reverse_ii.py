'''
92. Reverse Linked List II
Link: https://leetcode.com/problems/reverse-linked-list-ii/
Resource: https://bit.ly/3ai2PdI

Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> NULL, m = 2, n = 4
Output: 1 -> 4 -> 3 -> 2 -> 5 -> NULL
'''


class ListNode:

    def __int__(self, data):
        self.data = data
        self.next = None


def reverseBetween_v1(head, left: int, right: int):
    dummy = ListNode(0, head)
    prev, curr = dummy, head

    # find reversal point
    i = 1
    while i < left:
        prev = curr
        curr = curr.next
        i += 1

    before_reversal = prev
    start_of_reversal = curr

    # reverse section
    while i <= right:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        i += 1
    
    # calibrate
    before_reversal.next = prev
    start_of_reversal.next = curr

    return dummy.next


def reverseBetween_v2(head, left, right):
    '''
    1. https://www.youtube.com/watch?v=wk8-_M-2fzI&t=0s
    2. https://bit.ly/3ai2PdI
    '''

    dummy = ListNode(0, head)

    # find the position before reversal
    prev, curr = dummy, head
    for _ in range(left - 1):
        curr = curr.next
        prev = prev.next

    # reverse
    for _ in range(right - left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next
