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
            print(cur_node.data, end=' ')
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

    def remove_duplicates(self):
        '''
        1 - 6 - 1 - 4 - 2 - 2 - 4
        Then the desired resulting singly linked list should take the form:
        1 - 6 - 4 - 2
        '''
        curr = self.head
        prev = None

        _hash = set()

        while curr:
            temp = curr.next
            if curr.data in _hash:
                # Remove node:
                prev.next = curr.next
                curr = None
            else:
                # Have not encountered element before.
                _hash.add(curr.data)
                prev = curr

            curr = temp


llist = LinkedList()
llist.append(1)
llist.append(6)
llist.append(1)
llist.append(4)
llist.append(2)
llist.append(2)
llist.append(4)

llist.remove_duplicates()
llist.print_list()