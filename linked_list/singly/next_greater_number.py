'''
1019. Next Greater Node In Linked List
https://leetcode.com/problems/next-greater-node-in-linked-list/description/

You are given the head of a linked list with n nodes.
For each node in the list, find the value of the next greater node. 
That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.
Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). 
If the ith node does not have a next greater node, set answer[i] = 0.

Example 1:
Input: head = [2, 1, 5]
Output: [5, 5, 0]

Example 2:
Input: head = [2, 7, 4, 3, 5]
Output: [7, 0, 5, 5, 0]
'''

def nextLargerNodes(head) -> list[int]:
    # Convert the linked list to a list
    lst, curr = [], head
    while curr:
        lst.append(curr.val)
        curr = curr.next
    
    # Initialize variables
    res = [0] * len(lst)
    stack = []

    # Iterate through the list to find next larger nodes
    for i, curr_val in enumerate(lst):
        while stack and lst[stack[-1]] < curr_val:
            prev_idx = stack.pop()
            res[prev_idx] = curr_val
        stack.append(i)

    return res

def nextLargerNodes_v2(head) -> list[int]:
    res, stack = [], []
    curr, idx = head, 0

    while curr:
        res.append(0)
        curr_val = curr.val
        
        while stack and stack[-1][1] < curr_val:
            prev_idx, _ = stack.pop()
            res[prev_idx] = curr_val
        stack.append((idx, curr_val))
        
        idx += 1
        curr = curr.next

    return res