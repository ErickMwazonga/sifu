'''
876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/

Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: [1,2,3,4,5] -> 3
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

Example 2:
Input: [1,2,3,4,5,6] -> 4
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def middleNode(self, head):
        count = self.get_length(head)
        midpoint = count // 2

        curr = head
        i = 0

        while i < midpoint:
            curr = curr.next
            i += 1

        return curr

    def get_length(self, head):
        count = 0

        while head:
            count += 1
            head = head.next

        return count


def middleNode(head):
    fast, slow = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
