'''
82. Remove Duplicates from Sorted List II
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1, 2, 5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2, 3]
'''


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Node) -> Node:
        counter = {}

        curr = head
        while curr:
            val = curr.val
            counter[val] = counter.get(val, 0) + 1
            curr = curr.next

        dummy = Node(0, head)

        prev, curr = dummy, head
        while curr:
            freq = counter[curr.val]

            if freq > 1:
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next

        return dummy.next
