'''
LeetCode 234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Could you do it in O(n) time and O(1) space?
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def is_palindrome(sel, head):
        reversed_head = self.reverse(head)

        while head and reversed_head:
            if head.val != reversed_head.val:
                return False
            
            head = head.next
            reversed_head = reversed_head.next
        
        return True
    
    def isPalindrome(self, head):
        vals = []
        while head:
            vals += head.val
            head = head.next
        
        return vals == vals[::-1]

    def reverse(self, head):
        prev_node = None
        curr_node = head
        next_node = None

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        
        return prev_node