def middleNode(self, head):
    fast, slow = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
