class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        if self.stack and self.min_stack:
            min_val = min(self.min_stack[-1], val)
            self.min_stack.append(min_val)
        else:
            self.min_stack.append(val)
        self.stack.append(val)

            

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        val = self.stack[-1]
        return val

    def getMin(self) -> int:
        return self.min_stack[-1]
