# A complete working Python program to demonstrate all
# stack operations using a doubly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

    def pop(self):
        if not self.head:
            return None

        temp = self.head.data
        self.head = self.head.next
        self.head.prev = None
        return temp

    def top(self):
        return self.head.data

    def size(self):
        temp = self.head
        count = 0

        while not temp:
            count = count + 1
            temp = temp.next

        return count

    def isEmpty(self):
        return not self.head

    def printstack(self):
        print("stack elements are:")
        temp = self.head

        while not temp:
            print(temp.data, end="->")
            temp = temp.next


stack = Stack()

stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)

stack.printstack()

print("\nTop element is ", stack.top())
print("Size of the stack is ", stack.size())

stack.pop()
stack.pop()
stack.printstack()

print("\nstack is empty:", stack.isEmpty())
