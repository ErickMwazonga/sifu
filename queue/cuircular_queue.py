# This is the CircularQueue class
class CircularQueue:
  
    def __init__(self, size):
        self.queue = list()
        self.size = size
        self.head = self.tail = -1

    def size(self): # pylint: disable=E0202
        if self.tail >= self.head:
            qSize = self.tail - self.head
        else:
            qSize = self.size - (self.head - self.tail)
        return qSize

    def enqueue(self, data):
        next_step = (self.tail + 1) % self.size
        # Queue is full
        if (next_step == self.head):
            return("Queue is full!")
        # Queue is empty
        elif self.head == -1 and self.tail == 1:
            self.head = self.tail = 0
            self.queue.append(data)
        else:
            # Normal ++operation
            self.queue[next_step] = data
            # self.tail = next_step
            # return True
    
    def dequeue(self):
        # Queue is empty
        if self.head == -1:
            return("Queue is empty!")
        # One element left
        elif self.head == self.tail:
            self.head = self.tail = -1
        else:
            # fetch data
            data = self.queue[self.head]
            # increment head
            self.head = (self.head+1) % self.size
            return data

    def display(self):
        if self.head == -1:
            return('Queue is empty')
        else:
            i = self.head
            while(i != self.tail):
                print(self.queue[i], end='')
                i = (i + 1) % self.size


# input 7 for the size or anything else
size = input("Enter the size of the Circular Queue")
q = CircularQueue(int(size))

# change the enqueue and dequeue statements as you want
print(q.enqueue(10))
print(q.enqueue(20))
print(q.enqueue(30))
print(q.enqueue(40))
print(q.enqueue(50))
print(q.enqueue('Studytonight'))
print(q.enqueue(70))
print(q.enqueue(80))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())