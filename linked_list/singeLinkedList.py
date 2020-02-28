class Node:
    """
    A node in a single linked list
    """

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self):
        """Create new SinglyLinkedList: 0(1) time"""
        self.head = None
    
    def __repr__(self):
        """Return string representation of the list: 0(n) time"""
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return f"[{', '.join(nodes)}]"

    def prepend(self, data):
        """Insert a new element at the beginning: 0(1) time"""
        self.head = Node(data=data, next=self.head)

    def append(self, data):
        """Insert a new element at the end: 0(n) time"""
        if not self.head:
            self.head = Node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data=data)

    def find(self, key):
        """
        Search for the first element with key, return element
        or None if does not exist: 0(n) time
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr

    def remove(self, key):
        """Remove first occurrence of the key: 0(n) time"""
        curr = self.head
        prev = None
        
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None: # Delete first element
            self.head = curr.next
        elif curr: # Delete the other nodes
            prev.next = curr.next
            curr.next = None

    def reverse(self):
        """Reverse the list in-place: 0(n) time"""
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node




lst = SinglyLinkedList()
# print(lst)

lst.prepend(23)
lst.prepend('a')
lst.prepend(42)
lst.prepend('X')
lst.append('the')
lst.append('end')

# print(lst)
print(lst.find('end'))
