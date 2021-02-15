class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeLoop(head: ListNode) -> bool:
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
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None

    return head
