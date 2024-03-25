'''
143. Reorder List
Link: https://leetcode.com/problems/reorder-list/

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

class ListNode:
    ...

class Solution:
    def reorderList(self, head: ListNode) -> None:
        middle = self.middle(head)
        second = self.reverse(middle.next)
        middle.next = None # Break the link between the first and second halves
        
        first, second = head, second
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
    
    def reorderListV2(self, head: ListNode) -> None:
        middle = self.middle(head)
        second = self.reverse(middle.next)
        middle.next = None # Break the link between the first and second halves
        
        # another approach
        first, second = head, second
        while second:
            nxt = first.next
            first.next = second
            first = second
            second = nxt

    def middle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev, curr= curr, nxt
        return prev
    