"""
FIFO
enqueue: To add a new data element at the rear of the queue.
dequeue: To remove an element from the front of the queue.
isEmpty: To return True if the queue is empty, else return False.
size: To check the size of the queue, in other words count the number
of elements in the queue and return it.
show: To print all the queue elements.
"""


class Queue:

    # Constructor creates a list
    def __init__(self):
        self.queue = list()

    # Adding elements to queue
    def enqueue(self, data):
        # Checking to avoid duplicate entry (not mandatory)
        if data not in self.queue:
            self.queue.append(data)
            return True
        return False

    # Removing the last element from the queue
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return ("Queue Empty!")
        # return False

    # check if queue is empty or not
    def isEmpty(self):
        if len(self.queue) > 0:
            return False
        return True

    # Getting the size of the queue
    def size(self):
        return len(self.queue)

    # printing the elements of the queue
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
