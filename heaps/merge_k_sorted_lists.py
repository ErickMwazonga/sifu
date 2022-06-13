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
  1 -> 4 -> 5,
  1 -> 3 -> 4,
  2 -> 6
]
merging them into one sorted list:
1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
'''

from heapq import heappop, heappush


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    '''Credit: https://www.youtube.com/watch?v=zLcNwcR6yO4'''

    heap = []

    for l in lists:
        while l:
            heappush(heap, l.val)
            l = l.next

    head, curr = None, None
    while heap:
        if not head:
            head = ListNode(heappop(heap))
            curr = head
        else:
            curr.next = ListNode(heappop(heap))
            curr = curr.next

    return head


def mergeKLists_v2(lists):
    heap = []

    for l in lists:
        while l:
            heappush(heap, l.val)
            l = l.next

    head = curr = ListNode(None)
    while heap:
        curr.next = ListNode(heappop(heap))
        curr = curr.next

    return head.next


def mergeKLists_v3(lists):
    '''https://www.youtube.com/watch?v=ptYUCjfNhJY'''

    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heappush(heap, (lst.val, i, lst))

    curr = dummy = ListNode(0)

    while heap:
        _, i, node = heappop(heap)
        curr.next = node
        curr = curr.next

        if node.next:
            heappush(heap, (node.next.val, i, node.next))

    return dummy.next
