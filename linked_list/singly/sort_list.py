'''
148. Sort List
https://leetcode.com/problems/sort-list/

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
    '''MERGE SORT'''

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
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        return mid

    def merge(self, list1, list2):
        new_head = tail = ListNode()

        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next

        tail.next = list1 or list2

        return new_head.next


class Solution_V2:
    def sortList(self, head):
        if not head or not head.next:
            return head

        # Split the list into two halfs
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(head)
        right = self.sortList(right)

        return self.merge(left, right)

    def getMid(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, list1, list2):
        new_head = tail = ListNode()

        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next

        tail.next = list1 or list2

        return new_head.next
