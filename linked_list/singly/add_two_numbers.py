'''
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
    Input: list1 = 3 -> 2 -> 1 -> null, list2 = 5 -> 9 -> 4 -> 3 -> null
    Output: 8 -> 1 -> 6 -> 3 -> null
        Explanation: 123 + 3495 = 3618
Example 2:
    Input: list1 = 1 -> 6 -> 5 -> 4 -> null, list2 = 4 -> 8 -> 2 -> 7 -> 9 -> null
    Output: 5 -> 4 -> 8 -> 1 -> 0 -> 1 -> null
        Explanation: 4561 + 97284 + 101845
'''


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode):
    curr = dummy = ListNode(0)
    carry = 0

    while l1 or l2:
        _sum = 0
        _sum += carry

        if l1:
            _sum += l1.val
            l1 = l1.next

        if l2:
            _sum += l2.val
            l2 = l2.next

        carry, val = divmod(_sum, 10)

        nxt = ListNode(val)
        curr.next = nxt
        curr = curr.next

    if carry > 0:
        curr.next = ListNode(carry)

    return dummy.next
