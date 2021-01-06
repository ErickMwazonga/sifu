def delete(self, key):
    cur = self.head

    while cur:
        if cur.data == key and cur == self.head:
            # Case 1: Head node, next points to null
            if not cur.next:
                cur = None 
                self.head = None
                return

            # Case 2: Head node, next points to a node
            else:
                nxt = cur.next
                cur.next = None 
                nxt.prev = None
                cur = None
                self.head = nxt
                return 

        elif cur.data == key:
            # Case 3: Middle node
            if cur.next:
                nxt = cur.next 
                prev = cur.prev
                prev.next = nxt
                nxt.prev = prev
                cur.next = None 
                cur.prev = None
                cur = None
                return

            # Case 4: Last Node
            else:
                prev = cur.prev 
                prev.next = None 
                cur.prev = None 
                cur = None 
                return

        cur = cur.next