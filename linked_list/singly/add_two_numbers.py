'''
2. Add Two Numbers
Link: https://leetcode.com/problems/add-two-numbers/

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


from typing import Optional


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    
    def reverse(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
     
    def add_two_numbers(l1: ListNode, l2: ListNode) -> Optional[ListNode]:
        curr = dummy = ListNode(0)
        carry = 0

        while l1 or l2:
            curr_sum = 0
            curr_sum += carry

            if l1:
                curr_sum += l1.val
                l1 = l1.next

            if l2:
                curr_sum += l2.val
                l2 = l2.next

            carry, val = divmod(curr_sum, 10)

            new_node = ListNode(val)
            curr.next = new_node
            curr = curr.next

        if carry > 0:
            curr.next = ListNode(carry)

        return dummy.next

    def add_two_numbers_v2(self, l1, l2) -> Optional[ListNode]:
        list1, list2 = [], []

        curr = l1
        while curr:
            list1.append(curr.val)
            curr = curr.next

        curr = l2
        while curr:
            list2.append(curr.val)
            curr = curr.next

        dummy = curr = ListNode(0)
        carry = 0
        while list1 or list2:
            _sum = 0

            if list1:
                _sum += list1.pop()

            if list2:
                _sum += list2.pop()

            _sum += carry
            carry, rem = divmod(_sum, 10)

            new_node = ListNode(rem)
            curr.next = new_node
            curr = curr.next

        if carry:
            curr.next = ListNode(1)

        return self.reverse(dummy.next)

