'''
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/description/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
Output: [1, 1, 2, 3, 4, 4, 5, 6]

Explanation: The linked-lists are:
[
  1 -> 4 -> 5,
  1 -> 3 -> 4,
  2 -> 6
]
merging them into one sorted list:
1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
'''

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    '''
    Time - O(n log k), Space - O(n)
    At each level of recursion, the number of nodes being merged is proportional to the total number of nodes in all the lists. 
    The number of levels in the recursion tree is logarithmic, as the input lists are divided in half at each level.

    Overall time complexity - O(n log k), where n is the total number of nodes in all the lists, and k is the number of lists.
    '''
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])

        middle = len(lists) // 2
        left = self.mergeKLists(lists[:middle])
        right = self.mergeKLists(lists[middle:])

        return self.mergeTwoLists(left, right)        

    def mergeTwoLists(self, list1, list2):
        dummy = curr = ListNode(0)

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 or list2
        return dummy.next