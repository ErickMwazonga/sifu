class Node:
    '''A node in a single linked list'''

    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        '''Create new SinglyLinkedList: 0(1) time'''
        self.head = None

    def printList(self):
        '''Return string representation of the list: 0(n) time'''
        nodes = []
        curr = self.head

        while curr:
            nodes.append(curr.data)
            curr = curr.next
        return nodes

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end="->")
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

    def size(self, head):
        if not head:
            return 0
        return 1 + self.size(head.next)

    def get_tail(self, head):
        curr = head

        while curr.next:
            curr = curr.next
        return curr
