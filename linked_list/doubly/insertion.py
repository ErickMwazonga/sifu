class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)

            curr = self.head
            while curr.next:
                curr = curr.next

            curr.next = new_node
            new_node.prev = curr
            new_node.next = None

    def prepend(self, data):
        if not self.head:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def add_after_node(self, key, data):
        curr = self.head

        while curr:
            if not curr.next and curr.data == key:
                self.append(data)
                return
            elif curr.data == key:
                new_node = Node(data)
                nxt = curr.next
                curr.next = new_node
                new_node.next = nxt
                nxt.prev = new_node

            curr = curr.next

    def add_before_node(self, key, data):
        curr = self.head

        while curr:
            if not curr.prev and curr.data == key:
                self.prepend(data)
            elif curr.data == key:
                new_node = Node(data)
                prev = curr.prev
                prev.next = new_node
                curr.prev = new_node
                new_node.next = curr

            curr = curr.next


dllist = DoublyLinkedList()

dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)
dllist.add_after_node(3, 6)
dllist.add_before_node(4, 9)
