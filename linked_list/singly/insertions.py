'''
SLIDES: https://docs.google.com/presentation/d/1TCTdhhAAisXc1g7O2uh3OwjkUXeYbt18nDR-ba_6WOs/edit
CODE: https://github.com/vprusso/youtube_tutorials/blob/master/data_structures/linked_list
VIDEO: https://www.youtube.com/watch?v=FSsriWQ0qYE&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=5
'''


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

        # List is empty
        if not self.head:
            self.head = new_node
            return

        # When list is not empty
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print('Previous node is not in the list')
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_nth(head, index, data):
        # Insert to empty list
        if not head:
            return Node(data)

        # Prepend node - Set new head
        if index == 0:
            new_node = Node(data)
            new_node.next = head
            return new_node

        count = 1
        curr = head
        while curr:
            if count == index:
                inserted_node = Node(data)
                inserted_node.next = curr.next
                curr.next = inserted_node
                break

            curr = curr.next
            count += 1

        if not curr:
            raise Exception()

        return head


llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')

llist.prepend('E')
llist.insert_after_node(llist.head.next, 'E')

llist.print_list()
