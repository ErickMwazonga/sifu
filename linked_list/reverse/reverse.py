class Node(object):
    def __init__(self, value: int, next_node: "Node" = None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return self.value


class LinkedList(object):
    def __init__(self, head: Node = None):
        self.head = head

    def reverse(self) -> None:
        if self.head is None:
            return

        previous_node = None
        current_node = self.head
        next_node = current_node.next

        while next_node is not None:
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            next_node = current_node.next

        self.head = current_node
        self.head.next = previous_node

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.value
            current_node = current_node.next