def delete_node(self, key):
    curr = self.head

    # Node to be deleted is head.
    if curr and curr.data == key:
        self.head = curr.next
        curr = None
        return

    # Node to be deleted is not head.
    prev = None
    while curr and curr.data != key:
        prev = curr
        curr = curr.next

    # Node not found
    if not curr:
        return

    prev.next = curr.next
    curr = None


def delete_node_at_pos(self, pos):
    curr = self.head

    # Node to be deleted is head.
    if pos == 0:
        self.head = curr.next
        curr = None
        return

    # Node to be deleted is not head.
    prev = None
    count = 0
    while curr and count != pos:
        prev = curr
        curr = curr.next
        count += 1

    # Node not found
    if not curr:
        return

    prev.next = curr.next
    curr = None
