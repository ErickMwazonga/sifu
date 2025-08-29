'''
708. Insert into a Sorted Circular Linked List

This problem involves a special kind of linked list called a Circular Linked List,
where the last element points back to the first, creating a closed loop. 
Your task is to insert a new value into the list so that the list's non-descending (sorted) order is maintained.

The nuances of this task are:
    1. The node you are given could be any node in the loop, not necessarily the smallest value.
    2. You may insert the new value into any position where it maintains the sort order.
    3. If the list is empty (i.e., the given node is null), you must create a new circular list that contains the new value and return it.

You're expected to return a reference to any node in the modified list.
'''

class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None

def insert_node_at_correct_position(node: ListNode, val: int) -> ListNode:
    node = ListNode(val)
    
    # list is empty
    if not node:
        node.next = node
        return node
    
    # other cases
    prev, curr = node, node.next
    while curr != node:
        at_edge = prev.val > curr.val and (val >= prev.val or val <= curr.val)
        if prev.val <= val <= curr.val or at_edge:
            break
        prev, curr = curr, curr.next

    prev.next = node
    node.next = curr
    return node

def insert_node_at_correct_position_v2(node: ListNode, val: int) -> ListNode:
    new_node = ListNode(val)

    # if list is empty
    if not node:
        new_node.next = new_node
        return new_node

    # if only one one node exists
    if node == node.next:
        node.next = new_node
        new_node.next = node
        return node
    
    # inserting at edge min/max
    curr = node
    while curr:
        if node == node.next and node.val > node.next.val:
            temp = curr.next
            curr.next = new_node
            new_node.next = temp
            break
        curr = curr.next

    # happy case - in between increasing nodes
    curr, nxt = node, node.next
    while not (curr.val <= val <= nxt.val):
        curr = curr.next
        nxt = curr.next
    
    temp = curr.next
    curr.next = new_node
    new_node.next = nxt