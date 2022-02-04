'''
Remove Cycle from Linked List | Linked List Problem

You have given a singly linked list if a linked list contains a cycle, 
then remove the cycle and return the same linked list. 
If there is no cycle, then return the same linked list.
'''


def removeLoop(head):
    slow = fast = head
    has_cycle = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            has_cycle = True
            break

    if has_cycle:
        slow = head

        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next

        # Make next of fast i.e last node of Linked List None.
        fast.next = None

    return head
