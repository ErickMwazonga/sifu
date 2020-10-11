class Node:
    '''A node in a single linked list'''

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self):
        '''Create new SinglyLinkedList: 0(1) time'''
        self.head = None

    def printList(self):
        '''Return string representation of the list: 0(n) time'''
        nodes = []
        curr = self.head

        while curr:
            nodes.append(curr.data)
            curr = curr.next
        return nodes

    def prepend(self, data):
        '''Insert at the beginning: 0(1) time'''
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        '''Insert at the end: 0(n) time'''
        new_node = Node(data)

        if not self.head:  # Empty List
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def insertAfter(self, node, data):
        ''' Insert after a node'''
        if node is None:
            return

        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node

    def find(self, key):
        '''
        Search for the first element with key, return element
        or None if does not exist: 0(n) time
        '''
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr

    def deleteNth(self, position):
        '''Remove first occurrence of the position: 0(n) time'''

        if self.head is None:  # Empty list
            return

        prev = None
        curr = self.head
        i = 0

        # If position if of the first element
        if position == 0:
            self.head = curr.next
            curr = None
            return

        # Find the key to be deleted
        while curr and i < position:
            i += 1
            prev = curr
            curr = curr.next

        if not curr:
            return 'Position beyond length of list'

        next = curr.next
        prev.next = next

    def deleteNode(self, data):
        '''Remove first occurrence of the data: 0(n) time'''
        curr = self.head
        prev = None

        while curr and curr.data != data:
            prev = curr
            curr = curr.next

        # Delete first element
        if prev is None:
            self.head = curr.next

        # Delete the other nodes
        elif curr:
            prev.next = curr.next
            curr.next = None

    def reverse(self):
        '''Reverse the list in-place: 0(n) time'''

        curr = self.head
        prev_node = None
        next_node = None

        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node

        self.head = prev_node
        return self.head


sll = SinglyLinkedList()

sll.prepend(23)
sll.prepend('a')
sll.prepend(42)
sll.prepend('X')
sll.append('the')
sll.append('end')


assert sll.printList() == ['X', 42, 'a', 23, 'the', 'end']
assert sll.deleteNth(10) == 'Position beyond length of list'
sll.deleteNth(3)
assert sll.printList() == ['X', 42, 'a', 'the', 'end']
sll.deleteNode('the')
assert sll.printList() == ['X', 42, 'a', 'end']
sll.reverse()
assert sll.printList() == ['end', 'a', 42, 'X']
