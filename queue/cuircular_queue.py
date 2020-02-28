# This is the CircularQueue class
class CircularQueue:
  
    def __init__(self, size):
        self.queue = list()
        self.size = size
        self.head = 0
        self.tail = 0

    def size(self): # pylint: disable=E0202
        if self.tail >= self.head:
            qSize = self.tail - self.head
        else:
            qSize = self.size - (self.head - self.tail)
        return qSize

    def enqueue(self, data):
        # Queue is full
        if ((self.tail + 1) % self.size == self.head):
            return("Queue is full!")