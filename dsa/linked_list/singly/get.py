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
        if not self.head:
            self.head = Node(data)
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = Node(data)

    def get_node(self, val):
        curr = self.head

        while curr:
            if curr.data == val:
                return curr
            curr = curr.next

        raise ValueError('Not Found')

    def get_node_R(self, val):
        if not self.head:
            return False

        if self.head.val == val:
            return True

        return self.get_node_R(val)

    def get_ith(self, head, i):
        if i < 0:
            raise ValueError('No negatives!!! 🐱')

        idx, curr = 0, head
        while curr:
            if idx == i:
                return curr

            curr = curr.next
            idx += 1

        raise ValueError('Not Found')

    def get_ith_R(self, head, index):
        if not head:
            return None

        if index == 0:
            return head

        return self.get_ith_R(head.next, index-1)


llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')

llist.print_list()
