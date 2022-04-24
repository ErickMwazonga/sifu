'''
83. Remove Duplicates from Sorted List
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.

Examples
1. [1,1,2] -> [1,2]
2. [1,1,2,3,3] -> [1,2,3]
'''


def remove_duplicates(head):
    curr = head
    prev = None

    _hash = set()

    while curr:
        if curr.val in _hash:
            prev.next = curr.next
        else:
            _hash.add(curr.val)
            prev = curr

        curr = curr.next

    return head


def deleteDuplicates(head):
    curr = head

    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head
