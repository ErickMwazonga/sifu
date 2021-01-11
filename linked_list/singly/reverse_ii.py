'''
92. Reverse Linked List II
https://leetcode.com/problems/reverse-linked-list-ii/

Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''

# REVERSE 1
def reverse():
    if not self.head:
        return

    prev, curr, _next = None, self.head, None

    while curr:
        _next = curr.next
        curr.next = prev
        prev = curr
        curr = _next

    return prev


 def reverseBetween(head: ListNode, m, n):
    '''https://www.youtube.com/watch?v=wk8-_M-2fzI&t=0s'''

    if not head:
        return None

    dummy = ListNode(0)
    dummy.next = head
    
    curr, prev = head, dummy
    for _ in range(m - 1):
        curr = curr.next
        prev = prev.next
        
    for _ in range(n - m):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp
        
    return dummy.next