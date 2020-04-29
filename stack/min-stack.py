class MinStack:
    def __init__(self):
        self.data = []
        self.minData = []

    def push(self, x):
        self.data.append(x)
        # Check if we need to update the minimum value
        if len(self.minData) == 0 or x <= self.minData[-1]:
            self.minData.append(x)
            self.min = x

    def pop(self):
        if not len(self.data):
            return None
        else:
            if self.data[-1] == self.minData[-1]:
                self.minData.pop()
            return self.data.pop()

    def top(self):
        return self.data[-1] if len(self.data) else None
        # if not len(self.data):
        #     return None
        # else:
        #     return self.data[-1]

    def getMin(self):
        if not len(self.minData):
            return None
        else:
            return self.minData[-1]
