'''
148. Sort List
Link: https://leetcode.com/problems/sort-list/

Given the head of a linked list, return the list after sorting it in ascending order.

Examples:
1. [4, 2, 1, 3] -> [1, 2, 3, 4]
2. [-1, 5, 3, 4, 0] -> [-1, 0, 3, 4, 5]
3. [] -> []
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    '''BUBBLE SORT - Time: O(n^2), Space: O(n)'''

    def sortList(list):
        i = list.head

        while i:
            j = list.head

            while j.next:
                if j.data > j.next.data:
                    j.data, j.next.data = j.next.data, j.data

                j = j.next
            i = i.next


class Solution_v2:
    '''MERGE SORT - Time: O(nlogn), Space: O(logn)'''

    def sortList(self, head):
        if not head or not head.next:
            return head

        # Split the list into two halfs
        # left = head
        right = self.getMid(head)
        # tmp = right.next
        # right.next = None
        # right = tmp

        left = self.sortList(head)
        right = self.sortList(right)

        return self.merge(left, right)

    def getMid(self, head):
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        return mid

    def merge(self, list1, list2):
        new_head = curr = ListNode()

        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next

            curr = curr.next

        curr.next = list1 or list2

        return new_head.next
