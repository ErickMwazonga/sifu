class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def len_iterative(self):
        count = 0
        curr = self.head

        while curr:
            count += 1
            curr = curr.next
        return count

    def len_recursive(self, node):
        if not node:
            return 0
        return 1 + self.len_recursive(node.next)


llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')

print(llist.len_recursive(llist.head))
print(llist.len_iterative())
