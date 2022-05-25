'''
225. Implement Stack using Queues
Link: https://leetcode.com/problems/implement-stack-using-queues/

Implement a last in first out (LIFO) stack using only two queues.
The implemented stack should support all the functions of a normal queue (push, top, pop, and empty).

Implement the MyStack class:
void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
'''

from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, x):
        self.stack.append(x)
        n = len(self.stack)

        # make new element on the head position by rotation
        for _ in range(n-1):
            popped = self.stack.popleft()
            self.stack.append(popped)

    def pop(self):
        return self.stack.popleft()

    def top(self):
        return self.stack[0]

    def empty(self):
        return not self.stack
