class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def get_node(self, val):
        '''
        Search for the first element with val, return element
        or None if does not exist: 0(n) time
        '''
        curr = self.head
        while curr:
            if curr.data == val:
                return curr
            curr = curr.next

        raise ValueError('Not Found')

    def get_ith(head, i):
        if i < 0:
            raise ValueError('No negatives!!! 🐱')

        curr = head
        position = 0

        while curr:
            if position == i:
                return curr

            curr = curr.next
            position += 1

        raise ValueError('Not Found')


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.print_list()
