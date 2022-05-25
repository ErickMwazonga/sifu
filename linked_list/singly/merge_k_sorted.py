'''
23. Merge k Sorted Lists
Link: https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
'''

from heapq import heappop, heappush


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    heap = []

    for lst in lists:
        while lst:
            heappush(heap, lst.val)
            lst = lst.next

    dummy = ListNode(0)
    curr = dummy

    while heap:
        smallest = heappop(heap)
        curr.next = ListNode(smallest)
        curr = curr.next

    return dummy.next


def mergeKLists_v2(lists):
    '''
    https://www.youtube.com/watch?v=ptYUCjfNhJY
    Space: O(k). k is len(lists), Time: O(n * log(k)). n is total nodes
    '''

    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heappush(heap, (lst.val, i, lst))

    dummy = ListNode(0)
    curr = dummy

    while heap:
        _, i, node = heappop(heap)
        curr.next = node
        curr = curr.next

        if node.next:
            heappush(heap, (node.next.val, i, node.next))

    return dummy.next
