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

        previous_node = None
        current_node = self.head
        next_node = None

        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node
        # return previous_node

    def reverse_recursive(self):
        def helper(current_node, previous_node):
            if not current_node:
                return previous_node

            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            
            return helper(curr, prev)

        self.head = helper(current_node=self.head, previous_node=None)


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

#llist.reverse_iterative()
llist.reverse_recursive()

llist.print_list()