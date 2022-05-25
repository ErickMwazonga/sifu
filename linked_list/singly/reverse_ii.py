'''
92. Reverse Linked List II
Link: https://leetcode.com/problems/reverse-linked-list-ii/
Credit: https://bit.ly/3ai2PdI

Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''


class ListNode:

    def __int__(self, data):
        self.data = data
        self.next = None


def reverseBetween(head, left: int, right: int):
    dummy = ListNode(0)
    dummy.next = head

    leftprev, curr = dummy, head

    for _ in range(left-1):
        leftprev, curr = curr, curr.next

    prev = None
    for _ in range(right - left + 1):
        nxt = curr.next
        curr.next = prev
        prev = curr
        # curr = nxt

    leftprev.next.next = curr  # now 2's next is pointing to 5
    leftprev.next = prev  # 1's next pointer is poiting to 4

    return dummy.next


def reverseBetween_v2(head, m, n):
    '''
    1. https://www.youtube.com/watch?v=wk8-_M-2fzI&t=0s
    2. https://bit.ly/3ai2PdI
    '''

    dummy = ListNode(0)
    dummy.next = head

    # find the position
    curr, prev = head, dummy
    for _ in range(m-1):
        curr = curr.next
        prev = prev.next

    # reverse
    for _ in range(n-m):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next
