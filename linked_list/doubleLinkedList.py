class Node:
    """
    A node in a single linked list
    """

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class DoublyLinkedList:
    def __init__(self):
        """Create new DoublyLinkedList: 0(1) time"""
        self.head = None

    def __repr__(self):
        """Return string representation of the list: 0(n) time"""
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return f"[{', '.join(nodes)}]"

