class Node:
    '''A node in a single linked list'''

    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        '''Create new SinglyLinkedList: 0(1) time'''
        self.head = None

    def print_node_list(self):
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

    def generate_list(metadata=None):
        '''
        metadata = {
            'head': 0,
            "nodes": [
                {'value': 0, nxt: 1},
                {'value': 1, nxt: 2},
                {'value': 2, nxt: 3},
                {'value': 3, nxt: 4},
                {'value': 4, nxt: 5},
                {'value': 5, nxt: 6},
                {'value': 6, nxt: None}
            ]
        }
        '''
        head = None

        nodes = metadata["nodes"]
        for node in nodes:
            val, nxt = node["value"], node["nxt"]

            curr_node = Node(val)
            curr_node.next = nxt

            if val == metadata["head"]:
                head = curr_node

        return head

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
