'''
622. Design Circular Queue

Design your implementation of the circular queue.
The circular queue is a linear data structure in which the operations
are performed based on FIFO (First In First Out) principle and the
last position is connected back to the first position to make a circle.
It is also called "Ring Buffer".

Implementation the MyCircularQueue class:
MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
'''


class CircularQueue:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.size = 0
        self.max_size = k
        self.front = self.rear = -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.rear]

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max_size

        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        elif self.front == self.rear:  # One element left
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size

        self.size -= 1
        return True
