class MyCircularQueue:
    def __init__(self, k):
        self.list = [None] * k
        self.k = k
        self.front = self.rear = -1
        self.size = 0

    def enQueue(self, value):
        if self.isFull():
            return False
        else:
            self.front = (self.front + 1) % self.k
            self.list[self.front] = value
            self.size += 1
            return True

    def deQueue(self):
        if self.isEmpty():
            return False
        else:
            self.rear = (self.rear + 1) % self.k
            self.list[self.rear] = None
            self.size -= 1
            return True

    def Front(self):
        if self.isEmpty():
            return -1
        else:
            start = (self.rear + 1) % self.k
            return self.list[start]

    def Rear(self):
        if self.isEmpty():
            return -1
        else:
            return self.list[self.front]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.k


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
