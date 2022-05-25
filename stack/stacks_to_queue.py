'''
232. Implement Queue using Stacks
Link: https://leetcode.com/problems/implement-queue-using-stacks/

Implement a first in first out (FIFO) queue using only two stacks.
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
'''


class MyQueue:

    def __init__(self):
        self.inbox = []
        self.outbox = []

    def push(self, x: int) -> None:
        self.inbox.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1

        if self.outbox:
            return self.outbox.pop()
        else:
            while self.inbox:
                popped = self.inbox.pop()
                self.outbox.append(popped)

            return self.outbox.pop()

    def peek(self) -> int:
        if self.empty():
            return -1

        if self.outbox:
            return self.outbox[-1]
        else:
            while self.inbox:
                popped = self.inbox.pop()
                self.outbox.append(popped)

            return self.outbox[-1]

    def empty(self) -> bool:
        return not self.inbox and not self.outbox


class QueueFromTwoStacks:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def is_empty(self):
        return not self.in_stack and not self.out_stack

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                popped = self.in_stack.pop()
                self.out_stack.append(popped)

        return self.out_stack.pop()
