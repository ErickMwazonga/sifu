class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_loop(head: ListNode) -> ListNode:
    slow = fast = head
    has_cycle = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return head

    slow = head
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next
    fast.next = None

    return head
