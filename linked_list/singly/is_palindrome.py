'''
LeetCode 234. Palindrome Linked List
Link: https://leetcode.com/problems/palindrome-linked-list/

Given a singly linked list, determine if it is a palindrome.

Examples
1. 1 -> 2   = false
2. 1 -> 2 -> 2 -> 1  = true

Could you do it in O(n) time and O(1) space?
'''


def isPalindrome(head):
    vals = []

    while head:
        vals.append(head.val)
        head = head.next

    return vals == vals[::-1]


def isPalindrome_v2(head):
    vals = []

    while head:
        vals.append(head.val)
        head = head.next

    left, right = 0, len(vals)
    while left < right:
        if vals[left] != vals[right]:
            return False

    return True


class Solution_V3:
    def reverse(self, head):
        prev_node, curr_node = None, head

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        return prev_node

    def is_palindrome(self, head):
        reversed_head = self.reverse(head)

        while head and reversed_head:
            if head.val != reversed_head.val:
                return False

            head = head.next
            reversed_head = reversed_head.next

        return True


def isPalindromeList_v4(self, head):
    '''REVERSE ONLY THE RIGHT HALF'''

    # Find middle
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    first, second = head, self.reverse(slow)

    # Compare the two halves
    while first:
        if first.data != second.data:
            return False

        first = first.next
        second = second.next

    return True
