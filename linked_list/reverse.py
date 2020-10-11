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
        if not self.head:
            return

        previous_node = None
        current_node = self.head
        next_node = None

        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        return previous_node

    def reverse_2(self, head):        
        prev = None
                
        dummy = ListNode(0)
        dummy.next = head
        current = head
                
        while (current != None):
            new = ListNode(current.val)
            new.next = prev
            prev = new
            current = current.next
        
        head = dummy.next
        
        return prev

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.value
            current_node = current_node.next