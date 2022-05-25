'''
138. Copy List with Random Pointer
Link: https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. 
Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. 
None of the pointers in the new list should point to nodes in the original list.
For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
Return the head of the copied linked list.
The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

Example 1
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
'''


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head):
    if not head:
        return None

    mapping = {}
    curr = head

    while curr:
        mapping[curr] = Node(curr.val)
        curr = curr.next

    for node in mapping:
        copy = mapping[node]
        if node.next:
            copy.next = mapping[node.next]
        if node.random:
            copy.random = mapping[node.random]

    return mapping[head]


def copyRandomList_v2(head):
    old_to_copy = {None: None}

    curr = head
    while curr:
        copy = Node(curr.val)
        old_to_copy[curr] = Node(curr.val)
        curr = curr.next

    curr = head
    while curr:
        copy = old_to_copy[curr]
        copy.next = old_to_copy[curr.next]
        copy.random = old_to_copy[curr.random]
        curr = curr.next

    return old_to_copy[head]
