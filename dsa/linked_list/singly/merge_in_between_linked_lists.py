'''
1669. Merge In Between Linked Lists
https://leetcode.com/problems/merge-in-between-linked-lists/description/

You are given two linked lists: list1 and list2 of sizes n and m respectively.
Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:
Build the result list and return its head.

Example 1:
Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [10,1,13,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

Example 2:
Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
Explanation: The blue edges and nodes in the above figure indicate the result.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Find the nodes at positions a-1 and b+1
        first = self.find_node_at_position(list1, a - 1)
        last = self.find_node_at_position(list1, b + 1)

        # Connect the last node of list2 to the node at position b+1
        list2_tail = self.get_tail(list2)
        list2_tail.next = last

        # Connect the node at position a-1 to list2
        first.next = list2

        return list1

    def find_node_at_position(self, head: ListNode, position: int) -> ListNode:
        curr = head
        for _ in range(position):
            curr = curr.next
        return curr

    def get_tail(self, head: ListNode) -> ListNode:
        curr = head
        while curr.next:
            curr = curr.next
        return curr

    def mergeInBetween2(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr = list1
        first, last = None, None
        i = 0

        while curr:
            if i == a - 1:
                first = curr
            if i == b + 1:
                last = curr

            i += 1
            curr = curr.next

        first.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = last

        return list1

        