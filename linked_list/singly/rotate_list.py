'''
Given the head of a linked list, rotate the list to the right by k places.
Link: https://leetcode.com/problems/rotate-list/
Resource: https://www.youtube.com/watch?v=9VPm6nEbVPA
 
Example 1:
Input: head = [1, 2, 3, 4, 5],  k = 2
Output: [4, 5, 1, 2, 3]

Example 2:
Input: head = [0, 1, 2],  k = 4
Output: [2, 0, 1]
'''


def rotateRight(self, head, k: int):
    if not head or not head.next:
        return head

    # compute length
    n, curr = 1, head

    while curr.next:
        curr = curr.next
        n += 1

    # make it circular
    curr.next = head

    # go to the pivot
    k %= n  # incase of rotations more than n
    k = n - k - 1  # inorder not to go to next node

    curr = head
    while k:
        curr = curr.next
        k -= 1

    # break connection
    head = curr.next
    curr.next = None

    return head
