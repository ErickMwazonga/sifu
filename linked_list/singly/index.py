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

    def size(head):
        if not head:
            return 0
        return  1 + size(head.next)

    def get_tail(head):
        current_node = head

        while(current_node.next):
            current_node = current_node.next
        return current_node