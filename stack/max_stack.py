class MaxStack(object):

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, item):
        self.stack.push(item)

        if not self.max_stack:
            self.max_stack.append(item)
        else:
            last_max = self.max_stack[-1]

            if item >= lastmin:
                self.max_stack.append(item)
    
    def pop(self):
        item = self.stack.pop()

        # If it equals the top item in max_stack, they must have been pushed
        # in together. So we'll pop it out of max_stack too.
        if item == self.max_stack[-1]:
            self.max_stack.pop()

        return item

    def top(self) -> int:
        return self.stack[-1]

    def get_max(self):
        return self.max_stack[-1]