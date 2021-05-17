'''
142. Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

'''


class Solution:
    def detectCycle(self, head):
        slow = fast = head
        flag = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                flag = True
                break

        if flag:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next

            return slow

        return None
