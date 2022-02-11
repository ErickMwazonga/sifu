'''
24. Swap Nodes in Pairs
https://leetcode.com/problems/swap-nodes-in-pairs/

Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
 
Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    dummy = ListNode(0, head)
    prev, curr = dummy, head

    while curr and curr.next:
        # Sae pointers
        nxt_pair = curr.next.next
        second = curr.next

        # Reverse this pair
        second.next = curr
        curr.next = nxt_pair
        prev.next = second

        # Update pointers
        prev = curr
        curr = nxt_pair

    return dummy.next
