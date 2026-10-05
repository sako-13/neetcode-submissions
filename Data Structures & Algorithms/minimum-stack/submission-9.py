class MinStack:
    stack = []
    mstack = []
    def __init__(self):
        self.stack = []
        self.mstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mstack:
            val = min(val,self.mstack[-1])
        self.mstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.mstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mstack[-1]