def reverse(self):
    tmp = None
    cur = self.head

    while cur:
        tmp = cur.prev
        cur.prev = cur.next
        cur.next = tmp
        cur = cur.prev
        
    if tmp:
        self.head = tmp.prev
