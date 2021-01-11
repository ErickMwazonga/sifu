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

    def reverse_iterative(self):
        if not self.head:
            return

        prev = None
        curr = self.head
        _next = None

        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next

        self.head = prev
        # return self.head

    def reverse_recursive(self):
        def helper(curr, prev):
            if not curr:
                return prev

            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
            
            return helper(curr, prev)

        self.head = helper(curr=self.head, prev=None)


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

#llist.reverse_iterative()
llist.reverse_recursive()

llist.print_list()