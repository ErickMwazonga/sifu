'''
86. Partition List
Link: https://leetcode.com/problems/partition-list/

Given the head of a linked list and a value x, partition it such that all nodes less than x 
come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: [1, 4, 3, 2, 5, 2],  x = 3
Output: [1, 2, 2, 4, 3, 5]

Example 2:
Input: [2, 1],  x = 2
Output: [1, 2]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition(head, x: int):
    left_dummy, right_dummy = ListNode(0), ListNode(0)
    left, right = left_dummy, right_dummy

    while head:
        if head.val < x:
            left.next = head
            left = left.next
        else:
            right.next = head
            right = right.next

        head = head.next

    left.next = right_dummy.next
    right.next = None

    return left_dummy.next
