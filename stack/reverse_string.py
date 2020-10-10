from stack import Stack

def reverse(str):
    stack = Stack()
    reversed = ''

    for i in str:
        stack.append(i)

    for _ in stack:
        reversed = reversed + stack.pop()

    return reversed

print(reverse('Hello'))