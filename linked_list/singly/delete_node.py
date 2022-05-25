'''
237. Delete Node in a Linked List
Link: https://leetcode.com/problems/delete-node-in-a-linked-list/

Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, 
instead you will be given access to the node to be deleted directly.
It is guaranteed that the node to be deleted is not a tail node in the list.

Example 1:
Input: head = [4, 5, 1, 9],  node = 5
Output: [4, 1, 9]
'''


def deleteNode(node):
    next_node = node.next

    node.val = next_node.val
    node.next = next_node.next

    # del next_node
