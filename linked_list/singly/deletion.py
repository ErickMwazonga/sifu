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

    def delete_node(self, key):
        cur_node = self.head

        # Node to be deleted is head.
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        # Node to be deleted is not head.
        prev = None 
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        # Node not found
        if cur_node is None:
            return 

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        cur_node = self.head

        # Node to be deleted is head.
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        # Node to be deleted is not head.
        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node 
            cur_node = cur_node.next
            count += 1

        # Node not found
        if cur_node is None:
            return 

        prev.next = cur_node.next
        cur_node = None

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.delete_node("B")

llist.print_list()