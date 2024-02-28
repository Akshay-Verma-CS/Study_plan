class MinStack:

    def __init__(self):
        self.stack = []
        self.min = pow(2,64)

    def push(self, val: int) -> None:
        self.min = min(val, self.getMin() if len(self.stack) else val)
        self.stack.append([val,self.min])

    def pop(self) -> None:
        print("popped - ",self.stack.pop())
        print(self.stack)

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]