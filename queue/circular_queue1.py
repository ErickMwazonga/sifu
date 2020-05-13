# NOT WORKING YET
class MyCircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.currlen = 0
        self.head = self.tail = -1

    def isEmpty(self):
        return self.head == self.tail == -1

    def isFull(self):
        return (self.tail + 1) % self.size == self.head

    def Front(self):
        if self.isEmpty():
            return False
        return self.queue[self.head]

    def Rear(self):
        if self.isEmpty():
            return False
        return self.queue[self.tail]

    def enQueue(self, value):
        if self.isFull():
            return False

        if self.isEmpty():
            self.head = self.tail = 0
            self.queue[self.tail] = value
            return True
        else:
            next_step = (self.tail + 1) % self.size
            self.queue[next_step] = value
            return True

    def deQueue(self):
        if self.isEmpty():
            return False

        if self.head == self.tail:  # One element left
            self.head = self.tail = -1
        else:
            next_step = (self.tail + 1) % self.size
            print(self.head)
            self.head = next_step
            return True

    def display(self):
        if self.isEmpty():
            return False

        i = self.head
        while(i != self.tail):
            print(self.queue[i], end='')
            i = (i + 1) % self.size
        print(self.queue[self.tail])


cq = MyCircularQueue(3)  # set the size to be 3
assert cq.enQueue(1) == True
assert cq.enQueue(2) == True
assert cq.enQueue(3) == True
assert cq.enQueue(4) == False
assert cq.Rear() == 3
assert cq.isFull() == True
assert cq.deQueue() == True
assert cq.enQueue(4) == True
assert cq.Rear()  == 4
