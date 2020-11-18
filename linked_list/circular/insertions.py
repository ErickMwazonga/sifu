class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
    
        self.head = new_node

    def append(self, data):
        if not self.head: # No elements in the list
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            curr = self.head
            
            while curr.next != self.head: # Not at the end yet(Not last node)
                curr = curr.next

            curr.next = new_node
            new_node.next = self.head

    def print_list(self):
        curr = self.head

        while curr:
            print(curr.data, end=' ')
            curr = curr.next
            if curr == self.head:
                break


cllist = CircularLinkedList()
cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")
cllist.print_list()