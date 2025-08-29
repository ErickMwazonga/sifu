class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head

    def print_list(self):
        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next
            if curr == self.head:
                break

    def remove(self, key):
        # A single node in list
        if self.head.next == self.head and self.head.data == key:
            self.head = None
            return

        # Key is the head
        if self.head.data == key:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next
        else:
            curr = self.head
            prev = None

            while curr.next != self.head:
                prev = curr
                curr = curr.next

                if curr.data == key:
                    prev.next = curr.next
                    curr = curr.next

    def remove_node(self, node):
        if self.head == node:
            curr = self.head

            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next
        else:
            curr = self.head
            prev = None

            while curr.next != self.head:
                prev = curr
                curr = curr.next

                if curr == node:
                    prev.next = curr.next
                    curr = curr.next


cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")

cllist.remove("A")
cllist.remove("C")
cllist.print_list()
