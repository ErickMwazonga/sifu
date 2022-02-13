class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        curr = self.head

        # Node to be deleted is head.
        if curr and curr.data == key:
            self.head = curr.next
            curr = None
            return

        # Node to be deleted is not head.
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        # Node not found
        if not curr:
            return

        prev.next = curr.next
        curr = None

    def delete_node_at_pos(self, pos):
        curr = self.head

        # Node to be deleted is head.
        if pos == 0:
            self.head = curr.next
            curr = None
            return

        # Node to be deleted is not head.
        prev = None
        count = 0
        while curr and count != pos:
            prev = curr
            curr = curr.next
            count += 1

        # Node not found
        if not curr:
            return

        prev.next = curr.next
        curr = None


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.delete_node("B")

llist.print_list()
