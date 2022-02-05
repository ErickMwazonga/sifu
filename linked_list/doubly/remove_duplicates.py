def remove_duplicates(head):
    cur = head
    seen = dict()

    while cur:
        if cur.data not in seen:
            seen[cur.data] = 1
            cur = cur.next
        else:
            nxt = cur.next
            delete_node(cur)
            cur = nxt


def delete_node(head):
    pass
