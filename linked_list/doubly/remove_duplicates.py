def remove_duplicates(self):
    cur = self.head 
    seen = dict()
    
    while cur:
        if cur.data not in seen:
            seen[cur.data] = 1
            cur = cur.next
        else:
            nxt = cur.next
            self.delete_node(cur)
            cur = nxt