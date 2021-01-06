'''
641. Design Circular Deque
https://leetcode.com/problems/design-circular-deque/

Design your implementation of the circular double-ended queue (deque).
Your implementation should support following operations:

MyCircularDeque(k): Constructor, set the size of the deque to be k.
insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
getRear(): Gets the last item from Deque. If the deque is empty, return -1.
isEmpty(): Checks whether Deque is empty or not. 
isFull(): Checks whether Deque is full or not.
'''

class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.head = -1
        self.tail = 0
        self.data = [0]*k

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.capacity == self.size

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.tail]

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.head = (self.head + 1) % self.capacity
        self.data[self.head] = value
        self.size += 1
        return True
        
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.tail = (self.tail - 1) % self.capacity
        if self.head == -1:
            self.head = self.tail

        self.data[self.tail] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head-1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = (self.tail+1) % self.capacity
        self.size -= 1
        return True