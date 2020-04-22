'''
Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack.
If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently.
If there are no elements in the stack, then it should throw an error or return null.
'''

class Stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)
    
    def size(self):
        return len(self.items)

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack empty!")
        return self.items.pop()

    def isEmpty(self):
        return self.size() == 0

    def append(self, item):
        return self.items.append(item)
    
    def show(self):
        return self.items

# s = Stack()
# s.append('1')
# s.append('2')
# print(s.show())
