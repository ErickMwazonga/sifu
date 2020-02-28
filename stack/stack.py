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
