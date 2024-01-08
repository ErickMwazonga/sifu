'''
21. Merge Two Sorted Lists
Link: https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the ListNodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]
'''


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def mergeTwoLists(list1, list2):
    curr = dummy = ListNode(0)

    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next

        curr = curr.next

    curr.next = list2 or list2
    return dummy.next


def mergeTwoLists_v2(a, b):
    if a and b:
        if a.val > b.val:
            a, b = b, a
        a.next = mergeTwoLists(a.next, b)

    return a or b
