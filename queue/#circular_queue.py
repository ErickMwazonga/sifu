class CircularQueue:
    def __init__(self, k):
        self.maxlen = k
        self.currlen = 0
        self.queue = [None] * k
        self.head = self.tail = -1

    def isEmpty(self):
        return self.currlen == 0

    def isFull(self):
        return self.currlen == self.maxlen

    def Front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def enQueue(self, value):
        if self.isFull():
            return False

        next_step = (self.tail + 1) % self.maxlen
        self.tail = next_step
        self.currlen += 1

        self.queue[next_step] = value

        if self.currlen == 1:
            self.head = 0

        return True

    def deQueue(self):
        if self.isEmpty():
            return False

        to_remove = (self.head + 1) % self.maxlen
        self.head = to_remove
        self.currlen -= 1
        
        if self.currlen == 0:
            self.head = self.tail = -1

        return True

    def display(self):
        if self.isEmpty():
            return False

        i = self.head
        while(i != self.tail):
            print(self.queue[i], end=' ')
            i = (i + 1) % self.maxlen
        print(self.queue[self.tail])


cq = CircularQueue(3)
assert cq.enQueue(1) == True
assert cq.enQueue(2) == True
assert cq.enQueue(3) == True
assert cq.enQueue(4) == False
assert cq.Rear() == 3
assert cq.isFull() == True
assert cq.deQueue() == True
assert cq.enQueue(4) == True
assert cq.Rear()  == 4
cq.display()
