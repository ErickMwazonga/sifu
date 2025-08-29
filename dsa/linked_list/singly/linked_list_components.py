'''
817. Linked List Components
Link: https://leetcode.com/problems/linked-list-components/

You are given the head of a linked list containing unique integer values 
and an integer array nums that is a subset of the linked list values.
Return the number of connected components in nums where two values are 
connected if they appear consecutively in the linked list.

Example 1:
Input: head = [0,1,2,3], nums = [0,1,3]
Output: 2
Explanation: 0 and 1 are connected, so [0, 1] and [3] are the two connected components.

Example 2:
Input: head = [0,1,2,3,4], nums = [0,3,1,4]
Output: 2
Explanation: 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
'''


def numComponents(head, nums) -> int:
    nums = set(nums)
    count, connected = 0, False

    while head:
        if head.val in nums:
            if not connected:
                count += 1
                connected = True
        else:
            connected = False

        head = head.next

    return count


def numComponents_V2(head, nums) -> int:
    count, counted = 0, False
    _hash = set(nums)

    while head:
        if not counted:
            if head.val in _hash:
                count += 1
                counted = True
        else:
            if head.val not in _hash:
                counted = False

        head = head.next

    return count
