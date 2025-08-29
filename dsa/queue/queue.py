'''
QUEUE IMPLEMENTATION

FIFO
1. enqueue: To add a new data element at the rear of the queue.
2. dequeue: To remove an element from the front of the queue.
3. isEmpty: To return True if the queue is empty, else return False.
4. size: To count the number of elements in the queue and return it.
5. show: To print all the queue elements.
'''


class Queue:

    def __init__(self):
        self.queue = list()

    def enqueue(self, data):
        if data not in self.queue:
            self.queue.append(data)
            return True

        return False

    def dequeue(self):
        if not self.queue:
            return self.queue.pop(0)

        return ('Queue Empty!')

    def isEmpty(self):
        return not self.queue

    def size(self):
        return len(self.queue)

    def show(self):
        return self.queue


myQueue = Queue()
print(myQueue.enqueue(5))  # prints True
print(myQueue.enqueue(6))  # prints True
print(myQueue.enqueue(9))  # prints True
print(myQueue.enqueue(5))  # prints False
print(myQueue.enqueue(3))  # prints True
print(myQueue.size())      # prints 4
print(myQueue.dequeue())   # prints 5
print(myQueue.dequeue())   # prints 6
print(myQueue.dequeue())   # prints 9
print(myQueue.dequeue())   # prints 3
print(myQueue.size())      # prints 0
print(myQueue.dequeue())   # prints Queue Empty!
