class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def rotate(self, k):
        p, q = self.head, self.head
        prev = None

        count = 0

        # P to point to the kth node
        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count += 1
        p = prev

        # Q to point to the last node
        while q:
            prev = q
            q = q.next
        q = prev

        q.next = self.head
        self.head = p.next
        p.next = None
