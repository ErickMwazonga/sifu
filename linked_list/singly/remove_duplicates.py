'''
1 - 6 - 1 - 4 - 2 - 2 - 4
Then the desired resulting singly linked list should take the form:
1 - 6 - 4 - 2
'''


def remove_duplicates(self):
    curr = self.head
    prev = None

    _hash = set()

    while curr:
        temp = curr.next

        if curr.data in _hash:
            prev.next = curr.next
            curr = None
        else:
            _hash.add(curr.data)
            prev = curr

        curr = temp
