class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head

    def print_list(self):
        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next
            if curr == self.head:
                break

    def __len__(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
            if curr == self.head:
                break
        return count

    def remove_node(self, node):
        if self.head == node:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next
        else:
            curr = self.head
            prev = None

            while curr.next != self.head:
                prev = curr
                curr = curr.next

                if curr == node:
                    prev.next = curr.next
                    curr = curr.next

    def josephus_circle(self, step):
        curr = self.head

        while len(self) > 1:
            count = 1
            while count != step:
                curr = curr.next
                count += 1
            print("KILL:" + str(curr.data))
            self.remove_node(curr)
            curr = curr.next


cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)

cllist.josephus_circle(2)
cllist.print_list()
