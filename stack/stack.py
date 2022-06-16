'''
Implement a stack that has the following methods:

1. push(val), which pushes an element onto the stack
2. pop(), which pops off and returns the topmost element of the stack.
If there are no elements in the stack, then it should throw an error or return null.
3. max(), which returns the maximum value in the stack currently.
If there are no elements in the stack, then it should throw an error or return null.
'''


class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return not self.size()

    def show(self):
        return self.items


# s = Stack()
# s.append('1')
# s.append('2')
# print(s.show())
