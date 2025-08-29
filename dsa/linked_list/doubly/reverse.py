def reverse(head):
    prev, curr = None, head

    while curr:
        prev, nxt = curr.prev, curr.next
        curr.prev = nxt
        curr.next = prev
        curr = curr.prev

    head = prev.prev
