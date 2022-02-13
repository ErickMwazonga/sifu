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

        if not self.head:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def swap_nodes(self, key_1, key_2):
        '''
        Node_1 and Node_2 are not head nodes.
        Either Node_1 or Node_2 are head nodes.
        '''

        # Identical keys
        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        # One node does not exist
        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2  # First node is not the head
        else:
            self.head = curr_2  # Change the head

        if prev_2:
            prev_2.next = curr_1  # Second node is not the head
        else:
            self.head = curr_1  # Change the head

        # Update the next pointers
        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    ''' Alternate swap node function , swap by changing the data attribute of node '''

    def swap_nodes_alt(self, key_1, key_2):
        if key_1 == key_2:
            return

        curr = self.head
        x, y = None, None  # Assign None to avoid reference error

        while curr:
            if curr.data == key_1:
                x = curr  # key_1 found
            if curr.data == key_2:
                y = curr  # key_2 found
            curr = curr.next

        if x and y:  # Check if both key's exist
            x.data, y.data = y.data, x.data
        else:
            return


llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
llist.append('E')
llist.append('F')
llist.append('G')

print('Initial list')
llist.print_list()

print('swap by changing next attribute \n')
llist.swap_nodes('A', 'B')

llist.print_list()

print('swap by changing data attribute \n ')
llist.swap_nodes_alt('B', 'A')

llist.print_list()
