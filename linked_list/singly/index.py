class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def __init__(self, nodes=None):
        '''
        >>> llist = LinkedList(['a', 'b', 'c', 'd', 'e'])
        >>> llist => a -> b -> c -> d -> e -> None
        '''

        self.head = None

        if nodes:
            node = Node(data=nodes.pop(0))
            self.head = node

            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        '''>>> llist => a -> b -> c -> None'''

        node = self.head
        nodes = []

        while node:
            nodes.append(node.data)
            node = node.next

        nodes.append('None')
        return ' -> '.join(nodes)

    def get_nodes(self):
        nodes = []
        curr = self.head

        while curr:
            nodes.append(curr.data)
            curr = curr.next

        return nodes

    def prepend(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def append(self, data):
        new_node = Node(data)

        if not self.head:
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

    def generate_list(metadata=None):
        '''
        metadata = {
            'head': 0,
            'nodes': [
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

        nodes = metadata['nodes']
        for node in nodes:
            val, nxt = node['value'], node['nxt']

            curr_node = Node(val)
            curr_node.next = nxt

            if val == metadata['head']:
                head = curr_node

        return head
