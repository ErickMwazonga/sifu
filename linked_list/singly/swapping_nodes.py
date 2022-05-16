'''
1721. Swapping Nodes in a Linked List
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

You are given the head of a linked list, and an integer k.
Return the head of the linked list after swapping the values of the kth node 
from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
'''


class Solution:
    def swapNodes(self, head, k: int):
        n = self.length(head)

        front_kth = back_kth = head

        curr = head
        count = 1
        while curr:
            if count < k:
                front_kth = front_kth.next

            if count < n - k + 1:
                back_kth = back_kth.next

            count += 1
            curr = curr.next

        a, b = front_kth.val, back_kth.val
        front_kth.val, back_kth.val = b, a

        return head

    def length(self, head):
        count = 0

        while head:
            count += 1
            head = head.next

        return count


def swapNodes(head, k: int):
    first = head
    for _ in range(k - 1):
        first = first.next

    tmp, second = first, head
    while first.next:
        first = first.next
        second = second.next

    tmp.val, second.val = second.val, tmp.val

    return head
