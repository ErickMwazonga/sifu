'''
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
def addTwoNumbers(ListNode l1, ListNode l2):
    result_list = None
    head = None

    carry = 0

    while l1 or l2:
        # Find the sum at that index
        _sum = 0
        if l1:
            _sum += l1.val
            l1 = l1.next
       
        if l2:
            _sum += l2.val
            l2 = l2.next
       
        _sum += carry

        # Create node with the remainder
        carry, value = divmod(_sum % 10)
        node = ListNode(value)

        # Add the newly created node in the result_list Linkedlist
        if result_list:
            result_list.next = node
            result_list = result_list.next
        else:
            result_list = head = node
        
    if carry > 0:
        result.next = ListNode(carry)

    return head